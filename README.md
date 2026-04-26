# DEAL-RESCUE-AI-AGENT

AI-powered agent that detects at-risk deals and generates rescue email drafts for approval.

## Project Structure

```
├── frontend/          # React (Vite) dashboard
├── backend/           # FastAPI backend
│   ├── app/           # Application package
│   │   ├── ai/        # LLM integration (Groq/LangChain)
│   │   ├── api/       # API routes
│   │   ├── core/      # Config, JWT, security
│   │   ├── db/        # Database connection
│   │   ├── models/    # SQLAlchemy models
│   │   ├── schemas/   # Pydantic schemas
│   │   ├── services/  # Business logic
│   │   └── scripts/   # Utility scripts
│   └── main.py        # Entrypoint
├── build.sh           # Build script (frontend + backend)
├── start.sh           # Start script (uvicorn)
└── render.yaml        # Render deployment blueprint
```

## Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

The Vite dev server proxies `/api` requests to `localhost:8000`.

## Deploy to Render

1. Push to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com)
3. Click **New → Blueprint** and connect your repo
4. Render auto-detects `render.yaml` and creates the services
5. Add your secret env vars in the Render dashboard:
   - `GROQ_API_KEY`
   - `EMAIL`
   - `PASSWORD`
