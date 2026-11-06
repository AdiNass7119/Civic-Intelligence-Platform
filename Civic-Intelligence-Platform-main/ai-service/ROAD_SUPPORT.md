# Road Damage AI Support

The Civic Intelligence Platform now exposes the existing road-damage training class through the same AI pipeline used by the other civic issue classes.

## Integrated road dataset

`datasets/road_damage/` is included in the training corpus with the same image split size as the garbage dataset:

- Train: 140 images
- Validation: 30 images
- Test: 30 images
- COCO classes: `road-AibO`, `L00`, `R02`, `R03`

The integrated classifier is a four-class MobileNetV2 model and its label mapping is stored in `trained_models/label_mapping.json`:

- `garbage` → Garbage
- `road_damage` → Road Damage
- `street_light` → Street Light
- `water_leakage` → Water Leakage

## Runtime behavior

Road images are classified as **Road Damage** and routed to the **Roads & Buildings Department**. The existing API contract is preserved; road reports additionally expose `roadDamageLevel` and `issueMagnitude` so the existing severity and priority pipelines can operate without a separate integration path.

No separate frontend application, backend service, or AI endpoint is required for roads. The existing client → Express → FastAPI pipeline is reused.
