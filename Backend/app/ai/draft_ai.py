from langchain_core.prompts  import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.ai.llm_provider import llm

draft_prompt = PromptTemplate(
    input_variables=["email", "risk_type", "competitor"],
    template="""
You are a professional sales assistant replying to customer emails.

Your goal:
- Respond to the email in a helpful, polite, and confident tone
- Address the customer's concern based on the detected risk
- Keep the response short (2 to 5 lines)
- Encourage further conversation (e.g., offer help, demo, or clarification)

Context:
Customer Email:
{email}

Detected Risk:
- risk_type: {risk_type}
- competitor: {competitor}

Instructions:
- If competitor_mention → highlight strengths vs competitor without sounding negative
- If pricing_issue → justify value and flexibility
- If churn_risk → show empathy and try to retain the customer
- If no risk → respond politely and keep conversation open

Tone:
- Professional
- Friendly
- Confident (not aggressive)

IMPORTANT:
- Do NOT include explanations
- Do NOT include JSON
- Only return the final reply message

Output:
"""
)

parser = StrOutputParser()


draft_chain = draft_prompt | llm | parser


def generate_draft(email:str , risk_data:dict | None):
    if not risk_data:
        risk_type = "none"
        competitor = "none"
    else:
        risk_type = risk_data.get("risk_type","none")
        competitor = risk_data.get("competitor","none")

    response = draft_chain.invoke({
        "email":email,
        "risk_type":risk_type,
        "competitor":competitor
    })  

    return response.strip()      