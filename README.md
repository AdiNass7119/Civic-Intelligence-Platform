# AI-Powered Civic Intelligence Platform (APCIP)

### Smart Civic Issue Reporting, AI-Based Detection, Prioritization and Department Routing

![Project](https://img.shields.io/badge/Project-Civic%20Intelligence-blue)
![Frontend](https://img.shields.io/badge/Frontend-React%20%7C%20TypeScript-61DAFB)
![Backend](https://img.shields.io/badge/Backend-Node.js%20%7C%20Express-green)
![AI](https://img.shields.io/badge/AI-Python%20%7C%20FastAPI-orange)
![Database](https://img.shields.io/badge/Database-MongoDB-47A248)

---

## 1. Project Overview

The **AI-Powered Civic Intelligence Platform (APCIP)** is a smart civic management web application designed to improve how citizens report, monitor and resolve public infrastructure and sanitation problems.

Traditional complaint management systems depend heavily on manual inspection, manual classification and administrative decision-making. This platform introduces Artificial Intelligence to automate important stages of civic complaint processing.

Citizens can submit complaints with descriptions, images and location information. The AI service analyzes submitted complaints, identifies the type of civic issue, evaluates its severity, detects potential duplicates, predicts priority and recommends the appropriate government department.

The platform currently focuses on two major civic issue categories:

- **Garbage and Sanitation Management**
- **Road Damage Management**

The system provides separate interfaces for citizens, administrators and department officers, enabling transparent complaint tracking and coordinated civic operations.

## 2. Core Objectives

- Simplify civic complaint registration and tracking.
- Automate garbage and road damage identification using AI.
- Reduce manual complaint classification.
- Detect duplicate complaints and repeated reports.
- Estimate complaint severity and priority.
- Recommend the appropriate government department.
- Improve communication between citizens, administrators and field officers.
- Support data-driven civic administration and smarter city management.

## 3. Major Modules

### A. Garbage and Sanitation Management

The garbage management module allows citizens to report sanitation-related problems.

Supported use cases include:

- Garbage accumulation.
- Improper waste disposal.
- Illegal dumping.
- Unclean public spaces.
- Waste accumulation in residential and public areas.

AI-assisted processing includes image classification, garbage quantity assessment where supported, duplicate complaint detection, severity prediction and department recommendation.

The system routes sanitation complaints to the **Sanitation Department**.

### B. Road Damage Management

The road management module extends the platform to support road infrastructure complaints.

Supported use cases include:

- Potholes.
- Damaged road surfaces.
- Road deterioration.
- Cracks and other visible road damage.

Citizens can submit road-related complaints with supporting images, descriptions and location details.

The AI service analyzes road images, predicts road damage information where supported, evaluates severity and priority, and recommends the appropriate department.

The system routes road-related complaints to the **Roads & Buildings Department**.

### C. Citizen Dashboard

Citizens can:

- Register and log in.
- Submit civic complaints.
- Upload complaint images.
- Provide descriptions and location details.
- View submitted complaints.
- Monitor complaint status.
- Track complaint progress.
- Receive relevant notifications.

### D. Admin Dashboard

Administrators can:

- Monitor registered complaints.
- View and manage complaints.
- Filter complaints by category and status.
- Monitor garbage and road-related issues.
- Review AI-generated classifications and predictions.
- Manage complaint assignments and administrative workflows.
- Access platform analytics.

### E. Officer Dashboard

Department officers can:

- View assigned complaints.
- Review complaint details.
- Access relevant citizen-submitted images.
- Examine AI-generated complaint information.
- Manage assigned complaint workflows.
- Update complaint progress and resolution status.

## 4. AI Capabilities

The platform integrates an independent Python-based AI microservice.

The implemented AI processing pipeline includes:

| AI Component | Purpose |
|---|---|
| Image Classification | Identifies civic issue categories from submitted images |
| Duplicate Detection | Identifies potentially repeated complaints |
| Severity Prediction | Evaluates the seriousness of a complaint |
| Priority Prediction | Estimates complaint priority |
| Department Recommendation | Recommends the responsible department |
| Complaint Summarization | Generates a concise complaint summary |

### AI Processing Workflow

1. Citizen submits a complaint.
2. Complaint information and image references are passed to the backend.
3. Backend communicates with the AI microservice.
4. AI analyzes the submitted complaint.
5. Image classification identifies the issue category.
6. Duplicate detection checks for potentially similar complaints.
7. Severity and priority predictions are generated.
8. The appropriate department is recommended.
9. AI results are returned to the backend.
10. Complaint information is made available to the relevant dashboards.

**Department routing:**

- Garbage / Sanitation → Sanitation Department.
- Road Damage → Roads & Buildings Department.

AI predictions should be treated as decision-support information and can be reviewed by authorized personnel.

## 5. Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React, TypeScript, Vite |
| Styling | Tailwind CSS |
| UI and Animation | Lucide React, Framer Motion |
| Backend | Node.js, Express.js, TypeScript |
| AI Microservice | Python, FastAPI |
| Machine Learning | TensorFlow, NumPy, OpenCV |
| Database | MongoDB, Mongoose |
| API Communication | REST APIs, Axios |
| Authentication | JWT, bcrypt |
| Development Tools | VS Code, Git, GitHub |

## 6. System Architecture

```text
                 CITIZEN / ADMIN / OFFICER
                           |
                           |
                    REACT FRONTEND
                     Port: 3000
                           |
                           |
                    EXPRESS BACKEND
                     Port: 5000
                           |
              +------------+------------+
              |                         |
              |                         |
          MONGODB                 AI MICROSERVICE
         Database                  FASTAPI
                                   Port: 8000
                                      |
                    +-----------------+----------------+
                    |                 |                |
               Classification    Duplicate       Severity &
                  Pipeline       Detection         Priority
                    |                 |                |
                    +-----------------+----------------+
                                      |
                            Department Recommendation
                                      |
                             AI Analysis Response
                                      |
                              EXPRESS BACKEND
                                      |
                              MONGODB DATABASE
                                      |
                             DASHBOARD UPDATES
```

## 7. Project Directory Structure

```text
Civic-Intelligence-Platform/
│
├── client/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── dashboards/
│   │   ├── services/
│   │   └── ...
│   ├── .env.example
│   ├── package.json
│   └── vite.config.ts
│
├── server/
│   ├── src/
│   │   ├── config/
│   │   ├── database/
│   │   ├── modules/
│   │   ├── routes/
│   │   ├── middlewares/
│   │   └── server.ts
│   ├── docs/
│   ├── .env.example
│   └── package.json
│
├── ai-service/
│   ├── app/
│   │   ├── api/
│   │   ├── config/
│   │   ├── pipelines/
│   │   ├── models/
│   │   └── ...
│   ├── trained_models/
│   ├── datasets/
│   ├── requirements.txt
│   └── .env.example
│
├── .gitignore
└── README.md
```

## 8. Prerequisites

Install the following software before running the project.

| Software | Recommended version |
|---|---|
| Node.js | 18 or later |
| npm | Included with Node.js |
| Python | 3.10 or 3.11 |
| MongoDB | Local MongoDB or MongoDB Atlas |
| Git | Latest stable version |
| Visual Studio Code | Latest stable version |

Download links:

- Node.js: https://nodejs.org/
- Python: https://www.python.org/downloads/
- MongoDB: https://www.mongodb.com/try/download/community
- MongoDB Atlas: https://www.mongodb.com/products/platform/atlas-database
- Git: https://git-scm.com/downloads
- VS Code: https://code.visualstudio.com/

Check installations:

```powershell
node --version
npm --version
python --version
git --version
```

## 9. Clone the Repository

Open PowerShell or the VS Code terminal.

```powershell
git clone https://github.com/AdiNass7119/Civic-Intelligence-Platform.git
```

Navigate into the project:

```powershell
cd Civic-Intelligence-Platform
```

**Note:** If the repository contains a nested `Civic-Intelligence-Platform-main` directory, enter that directory before executing the remaining commands.

```powershell
cd Civic-Intelligence-Platform-main
```

All subsequent setup commands assume you are inside the directory containing `client`, `server` and `ai-service`.

## 10. Environment Configuration

The application requires environment variables for database connectivity, authentication and communication between services.

Create local environment files from the provided examples.

### Backend Environment

Open Terminal 1:

```powershell
cd server
Copy-Item .env.example .env
```

Open `server/.env` and configure:

```env
PORT=5000
NODE_ENV=development

MONGODB_URI=mongodb://127.0.0.1:27017/civic_intelligence

JWT_SECRET=replace_with_a_secure_random_secret

AI_SERVICE_URL=http://127.0.0.1:8000

FRONTEND_URL=http://localhost:3000
```

Use your actual MongoDB connection string if you are using MongoDB Atlas.

Generate a secure JWT secret rather than using the example placeholder.

### Frontend Environment

Open Terminal 2:

```powershell
cd client
Copy-Item .env.example .env
```

Configure `client/.env`:

```env
VITE_API_BASE_URL=http://localhost:5000/api/v1
```

### AI Service Environment

Open Terminal 3:

```powershell
cd ai-service
Copy-Item .env.example .env
```

Configure `ai-service/.env`:

```env
PORT=8000

NODE_API_URL=http://localhost:5000/api/v1

MONGODB_URI=mongodb://127.0.0.1:27017/civic_intelligence

DB_NAME=civic_intelligence
```

For MongoDB Atlas, use the appropriate connection string in both backend and AI service configurations.

**Important:** Never commit actual `.env` files, database passwords or API credentials to GitHub.

## 11. Installation and Execution

The platform consists of three independently running services.

Run each service in a separate VS Code terminal.

### Terminal 1 — Backend (Node.js + Express)

Navigate to the backend:

```powershell
cd server
```

Install dependencies:

```powershell
npm install
```

Start the backend development server:

```powershell
npm run dev
```

Expected service address:

```text
http://localhost:5000
```

Backend health check:

```text
http://localhost:5000/api/health
```

API documentation:

```text
http://localhost:5000/api/docs
```

### Terminal 2 — AI Microservice (Python + FastAPI)

Navigate to the AI service:

```powershell
cd ai-service
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.venv\Scripts\Activate.ps1
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install Python dependencies:

```powershell
pip install -r requirements.txt
```

Start the FastAPI service:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Expected service address:

```text
http://localhost:8000
```

AI health check:

```text
http://localhost:8000/api/v1/health
```

FastAPI interactive documentation:

```text
http://localhost:8000/docs
```

### Terminal 3 — Frontend (React + Vite)

Navigate to the frontend:

```powershell
cd client
```

Install dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

Expected frontend address:

```text
http://localhost:3000
```

Open the address in your browser.

## 12. Service Ports

| Service | Port | Local URL |
|---|---:|---|
| React Frontend | 3000 | http://localhost:3000 |
| Node.js Backend | 5000 | http://localhost:5000 |
| Python AI Service | 8000 | http://localhost:8000 |
| MongoDB | 27017 | mongodb://127.0.0.1:27017 |

## 13. Verify the Application

After starting all three services, verify the following:

**Frontend**

```text
http://localhost:3000
```

**Backend health**

```text
http://localhost:5000/api/health
```

**AI service health**

```text
http://localhost:8000/api/v1/health
```

**Backend to AI connectivity**

```text
http://localhost:5000/api/v1/system/ai-health
```

**Backend API documentation**

```text
http://localhost:5000/api/docs
```

**AI API documentation**

```text
http://localhost:8000/docs
```

Ensure MongoDB is running and both backend and AI service can connect to it.

## 14. Production Build

### Frontend Build

```powershell
cd client
npm run build
```

The production frontend build is generated in:

```text
client/dist/
```

### Backend Build

```powershell
cd server
npm run build
```

The compiled backend output is generated in:

```text
server/dist/
```

### AI Service

The AI service runs through Uvicorn. Its Python dependencies and trained model assets must be available in the deployment environment.

Production deployment requires configuring secure environment variables, database access, CORS and service URLs.

## 15. Common Troubleshooting

| Problem | Suggested solution |
|---|---|
| `npm is not recognized` | Install Node.js and restart the terminal |
| `python is not recognized` | Install Python and enable PATH configuration |
| MongoDB connection error | Verify MongoDB is running and check `MONGODB_URI` |
| Backend startup failure | Verify `server/.env` and required environment variables |
| AI service startup failure | Verify Python version and install `requirements.txt` |
| AI connection error | Verify `AI_SERVICE_URL` and ensure port 8000 is available |
| Frontend API error | Verify `VITE_API_BASE_URL` and backend availability |
| Missing Python module | Activate the virtual environment and reinstall dependencies |
| Port already in use | Stop the process using that port before restarting the service |

## 16. Important Development Notes

- Run the backend, frontend and AI microservice simultaneously.
- MongoDB must be available before the backend starts.
- The AI service requires its environment configuration and model assets.
- Do not delete trained model files required by the classification pipeline.
- Install dependencies separately inside `client`, `server` and `ai-service`.
- Do not upload `node_modules`, Python virtual environments or local secrets to GitHub.
- The project is intended to run as a coordinated multi-service application.

## 17. Future Enhancements

Potential future improvements include:

- Additional civic issue categories.
- Advanced road condition monitoring.
- Geospatial complaint visualization.
- GIS-based civic infrastructure mapping.
- Improved AI classification accuracy.
- Real-time complaint tracking.
- Mobile application integration.
- Advanced city-level analytics.
- Predictive maintenance and infrastructure planning.

## 18. Project Vision

The vision of the AI-Powered Civic Intelligence Platform is to connect citizens, administrators and government departments through intelligent technology.

By combining image-based issue detection, automated complaint analysis, duplicate identification, severity prediction and department routing, the platform aims to make civic problem reporting more efficient, transparent and data-driven.

**A smarter approach to cleaner surroundings, safer roads and better-managed cities.**

---

## Repository

**GitHub:** https://github.com/AdiNass7119/Civic-Intelligence-Platform

**Project:** AI-Powered Civic Intelligence Platform (APCIP)

**Primary Modules:** Garbage Management and Road Damage Management

**Architecture:** React Frontend + Node.js Backend + Python AI Microservice + MongoDB

