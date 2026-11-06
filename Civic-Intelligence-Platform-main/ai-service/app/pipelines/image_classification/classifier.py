import os
from typing import Dict, Any, Optional
from datetime import datetime, timezone
import tensorflow as tf
import numpy as np
import time

from app.utils.logger import logger
from app.utils.image_processing import preprocess_image
from app.services.model_loader import model_loader
from app.pipelines.base import BaseInferencePipeline


class ImageClassificationPipeline(BaseInferencePipeline):
    """
    Classifies a civic-issue image using the existing multi-class civic model.

    The original project was wired to expose only the Garbage class even though
    the trained model already contains Garbage, Road Damage, Street Light and
    Water Leakage classes.  This implementation preserves the existing API
    fields while exposing the complete model prediction.
    """

    DISPLAY_LABELS = {
        "garbage": "Garbage",
        "road_damage": "Road Damage",
        "street_light": "Street Light",
        "water_leakage": "Water Leakage",
    }

    def __init__(self, model_name: str = "civic_classifier"):
        self.model_name = model_name

    def preprocess(self, file_path: str) -> Optional[Any]:
        try:
            logger.info(f"Preprocessing image: {file_path}")
            tensor = preprocess_image(file_path, target_size=(224, 224), expand_dims=True)
            return tensor
        except Exception as e:
            logger.error(f"Error preprocessing {file_path}: {e}")
            raise

    @classmethod
    def _display_label(cls, raw_label: str) -> str:
        normalized = str(raw_label or "").strip().lower()
        return cls.DISPLAY_LABELS.get(normalized, normalized.replace("_", " ").title())

    @staticmethod
    def _magnitude_from_confidence(confidence: float) -> int:
        """Convert model confidence into a conservative 1..3 issue magnitude.

        This is deliberately kept as a compatibility field for the existing
        severity pipeline; it is not presented as a physical measurement.
        """
        if confidence >= 0.90:
            return 3
        if confidence >= 0.70:
            return 2
        return 1

    def _mock_result(self, processed_data: tf.Tensor) -> Dict[str, Any]:
        """Graceful fallback when the TensorFlow model is unavailable."""
        mock_confidence = 0.95
        tensor_mean = float(np.mean(processed_data)) if processed_data is not None else 0.0

        # Preserve the previous deterministic fallback for bright/no-issue test images.
        if tensor_mean > 0.94:
            category_name = "No Garbage"
            magnitude = 0
        else:
            category_name = "Garbage"
            magnitude = 2

        return {
            "processingStatus": "completed",
            "categoryPrediction": category_name,
            "garbageQuantity": magnitude if category_name == "Garbage" else 0,
            "issueMagnitude": magnitude,
            "confidence": mock_confidence,
            "message": f"MOCK: TensorFlow model not loaded. Predicted {category_name}.",
            "inferenceTimeMs": 50.0,
        }

    def infer(self, processed_data: Optional[tf.Tensor]) -> Dict[str, Any]:
        if processed_data is None:
            return {
                "processingStatus": "FAILED",
                "message": "Preprocessing failed or no data provided."
            }

        model = model_loader.get_model(self.model_name)
        if model is None:
            logger.warning(f"Classification model '{self.model_name}' is not available. Using mock.")
            return self._mock_result(processed_data)

        try:
            logger.info(f"Running real inference using model '{self.model_name}'...")
            start_time = time.time()
            predictions = model.predict(processed_data, verbose=0)
            end_time = time.time()

            inference_time_ms = (end_time - start_time) * 1000
            class_idx = int(np.argmax(predictions[0]))
            confidence = float(np.max(predictions[0]))

            # The model was trained from ai-service/datasets, whose sorted
            # top-level classes are represented by label_mapping.json.
            label_mapping = model_loader.get_label_mapping() or {}
            raw_label = label_mapping.get(str(class_idx), label_mapping.get(class_idx, "unknown"))
            raw_label = str(raw_label)
            category_name = self._display_label(raw_label)
            magnitude = self._magnitude_from_confidence(confidence)

            result: Dict[str, Any] = {
                "processingStatus": "completed",
                "categoryPrediction": category_name,
                "issueMagnitude": magnitude,
                "confidence": round(confidence, 4),
                "message": "Inference successful.",
                "inferenceTimeMs": round(inference_time_ms, 2),
            }

            # Keep the existing Garbage contract intact.  Road issues receive
            # the analogous roadDamageLevel field instead of pretending that
            # a road defect has a garbage quantity.
            if raw_label.lower() == "garbage":
                result["garbageQuantity"] = magnitude
            elif raw_label.lower() == "road_damage":
                result["roadDamageLevel"] = magnitude

            return result
        except Exception as e:
            logger.error(f"Inference error: {e}")
            return {
                "processingStatus": "FAILED",
                "message": str(e)
            }

    def postprocess(self, inference_result: Dict[str, Any]) -> Dict[str, Any]:
        status = inference_result.get("processingStatus", "FAILED")
        analysis = {
            "processingStatus": status,
            "analyzedAt": datetime.now(timezone.utc).isoformat(),
            "message": inference_result.get("message", "")
        }

        if status == "completed":
            for key in (
                "categoryPrediction",
                "garbageQuantity",
                "roadDamageLevel",
                "issueMagnitude",
                "confidence",
                "inferenceTimeMs",
            ):
                if key in inference_result:
                    analysis[key] = inference_result[key]

        return analysis

    def run(self, file_path: str) -> Dict[str, Any]:
        try:
            processed_data = self.preprocess(file_path)
            inference_result = self.infer(processed_data)
            return self.postprocess(inference_result)
        except Exception as e:
            logger.error(f"Pipeline execution failed: {e}")
            return {
                "processingStatus": "FAILED",
                "message": str(e),
                "analyzedAt": datetime.now(timezone.utc).isoformat()
            }
