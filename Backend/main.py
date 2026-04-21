from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

# ✅ CORS (keep localhost + add production later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5175",
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        # 👉 ADD THIS AFTER DEPLOY
        # "https://your-frontend.vercel.app"
    ],
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
    config = getAppConfig()
    return {
        "msg": "server is running",
        "app_name": config.app_name
    }


# ✅ Create tables (ok for now)
Base.metadata.create_all(bind=engine)


# ❌ REMOVE THIS FOR PRODUCTION (optional to keep for local dev)
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)