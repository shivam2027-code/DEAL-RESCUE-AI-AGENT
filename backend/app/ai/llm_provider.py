from langchain_groq import ChatGroq
from app.core.config import getAppConfig

config = getAppConfig()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=1.5,
    api_key=config.groq_api_key,
)
