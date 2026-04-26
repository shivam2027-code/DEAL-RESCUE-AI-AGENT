# check type of risk like comptitor mention , ghost

from app.db.database import sessionLocal
from app.models.risk_event import Risk




def create_risk(risk_type:str , competitor:str , event_id:int):
    db = sessionLocal()

    risk = Risk(
        risk_type = risk_type,
        competitor = competitor,
        event_id = event_id
        
    )

    db.add(risk)
    db.commit()
    db.refresh(risk)

    db.close()

    return risk.id
