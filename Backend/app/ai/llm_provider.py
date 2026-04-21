from langchain_groq import ChatGroq
from app.core.config import getAppConfig

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=1.5
)





