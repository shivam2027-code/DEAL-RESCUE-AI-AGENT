from langchain_core.prompts import  PromptTemplate
from langchain_core.runnables import Runnable
from langchain_core.output_parsers import StrOutputParser

import json
from app.ai.llm_provider import llm

parser = StrOutputParser()

detection_prompt = PromptTemplate(
    input_variables= ['email'],
    template= """
You are an AI assistant that analyzes business emails and detects risks.

Your task:
- Read the email carefully
- Identify if there is any risk
- If yes, classify the risk
- Extract relevant details

Risk types:
- competitor_mention → if user mentions competitors (e.g., Salesforce, HubSpot)
- pricing_issue → if user talks about price concerns
- churn_risk → if user shows disinterest or leaving intent
- none → if no risk detected

IMPORTANT:
- Always return output in STRICT JSON format
- Do NOT add any explanation
- Do NOT add extra text

Output format:
{{
  "risk_type": "<one of: competitor_mention | pricing_issue | churn_risk | none>",
  "competitor": "<competitor name if mentioned, else null>"
}}

Email:
{email}

Output:
"""
)


detection_chain = detection_prompt | llm | parser


def detect_risk(email:str):
    response = detection_chain.invoke({"email":email})
    print("raw llm output",response)

    try:
        response_str = str(response)
        risk_data = json.loads(response_str)
        if risk_data.get("risk_type")  == "none":
            return None
        return risk_data
    
    except Exception as e :
        print("json erroe",e)
        return None
        
    


