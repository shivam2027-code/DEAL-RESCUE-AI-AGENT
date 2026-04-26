from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os


# Routers
from app.api.routes.email import router as Email_router
from app.api.routes.draft import draft_router
from app.api.routes.approval import approve_router
from app.api.routes.auth import auth_router


# Config & DB
from app.core.config import getAppConfig
from app.db.database import Base, engine

# Models (important for table creation)
from app.models import risk_event, email_event, draft, user_model

# AI
from app.ai.llm_provider import llm

app = FastAPI()

config = getAppConfig()

# ✅ CORS — allow frontend dev server + production
allowed_origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://127.0.0.1:5174",
    "http://localhost:5174",
]

# Add the Render production URL if set
RENDER_URL = os.environ.get("RENDER_EXTERNAL_URL")
if RENDER_URL:
    allowed_origins.append(RENDER_URL)

# Add the deployed frontend URL to allowed origins
FRONTEND_URL = os.environ.get("FRONTEND_URL")
if FRONTEND_URL:
    allowed_origins.append(FRONTEND_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Routes
app.include_router(Email_router, prefix="/api")
app.include_router(draft_router, prefix="/api")
app.include_router(approve_router, prefix="/api")
app.include_router(auth_router, prefix="/api")


# ✅ Test LLM
@app.get("/llm")
def hello():
    response = llm.invoke("where is cricket born")
    return {"msg": response}


# ✅ Config test
@app.get("/config")
def secrets():
    return {
        "msg": "server is running",
        "app_name": config.app_name,
    }


# ✅ Create tables
Base.metadata.create_all(bind=engine)

# ✅ Serve React build (dist/ is copied here by build.sh)
dist_path = os.path.join(os.path.dirname(__file__), "dist")
if os.path.isdir(dist_path):
    app.mount("/", StaticFiles(directory=dist_path, html=True), name="static")

    @app.get("/{full_path:path}")
    async def serve_react(full_path: str):
        index = os.path.join(dist_path, "index.html")
        return FileResponse(index)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)