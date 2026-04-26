from fastapi import APIRouter , Request
from pydantic import BaseModel
from typing import Optional
from app.services.detection_service import detect_comptiter
from app.services.draft_service import save_draft
from app.services.event_service import create_event
from app.services.risk_service import  create_risk

from app.ai.detection_ai import detect_risk
from app.ai.draft_ai import generate_draft


router = APIRouter()

#schema for email

class EmailWebhook(BaseModel):
    email:str
    sender:str

@router.post("/email/incoming")
def email_process(data : EmailWebhook):
    email = data.email
    sender = data.sender

    #return {"msg":"recieved","email":data} 

    #return event id

    event_id  = create_event(email,sender)


    risk_data = detect_risk(email)

    risk_id = None

    if risk_data:
        risk_id = create_risk(
            risk_type = risk_data["risk_type"],
            competitor = risk_data["competitor"],
            event_id = event_id
        )

    reply = generate_draft(email ,risk_data)

    save_drafts = save_draft(reply,event_id)


    return {"event_id":event_id , 
            "risk":risk_data,               # it container competitor
            "reply":reply,
}
    
    


    
       




 
