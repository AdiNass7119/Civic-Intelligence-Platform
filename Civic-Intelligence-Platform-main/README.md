# AI-Powered Civic Intelligence Platform

A smart web application enabling citizens to report civic problems, with AI-driven triage, classification, and routing.

## Monorepo Structure

- `/client` - React + TypeScript + Vite frontend application.
- `/server` - Node.js + Express + TypeScript backend API.
- `/ai-service` - Python + FastAPI microservice for AI features.

## Getting Started

### Prerequisites
- Node.js (v18+)
- Python (3.9+)
- Docker (optional, for containerized execution)

### 1. Client Setup
```bash
cd client
npm install
npm run dev
```

### 2. Server Setup
```bash
cd server
npm install
npm run dev
```

### 3. AI Service Setup
```bash
cd ai-service
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Civic issue coverage
The existing AI pipeline supports multiple civic issue classes, including **Garbage** and **Road Damage**. Road-damage images are already included in `ai-service/datasets/road_damage/` and are classified through the same `civic_classifier.keras` model. Road predictions are routed to the Roads & Buildings Department without introducing a separate frontend, backend, or AI service.
