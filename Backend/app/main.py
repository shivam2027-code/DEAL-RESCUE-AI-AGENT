import uvicorn
from fastapi import FastAPI
from app.api.routes.email import router as Email_router
from app.api.routes.draft import draft_router
from app.api.routes.approval import approve_router
from app.api.routes.auth import auth_router
from app.core.config import getAppConfig
from app.db.database import  Base , sessionLocal , engine
from app.models import risk_event , email_event , draft , user_model
from app.ai.llm_provider import llm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5175",
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(Email_router , prefix="/api")
app.include_router(draft_router , prefix="/api")
app.include_router(approve_router , prefix="/api")
app.include_router(auth_router,prefix="/api")

@app.get("/llm")
def hello():
    response = llm.invoke(
    'where is the cricket born')
    return {"msg":response}


@app.get("/config")
def secrets():
    config = getAppConfig()

    return {"msg":"hello server is running" , "config":config.app_name}


Base.metadata.create_all(bind=engine)












if __name__ == "__main__":
    uvicorn.run("app.main:app",host="0.0.0.0",port=8000,reload=True)
