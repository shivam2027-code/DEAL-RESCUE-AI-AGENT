from fastapi import APIRouter , HTTPException
from app.db.database import sessionLocal
from app.models.draft import Draft
from app.services.email_service import send_email
from app.models.email_event import Event


approve_router =  APIRouter()

@approve_router.post("/draft/{id}/approve")
def approve_draft(id:int):
    db = sessionLocal()
    

    try:

        draft = db.query(Draft).filter(Draft.id == id).first()

        if not draft:

           raise HTTPException(status_code=404 , detail="draft not found")
    
        if draft.status == "approved":
           return {"msg":"draft approved"}
    
        draft.status = "approved"

        db.commit()

        # get event to fetch sender email

        event = db.query(Event).filter(Event.id == draft.event_id).first()

        if event:
            send_email(
                to_email=event.sender,
                subject="Re : your Inquiry",
                body=draft.reply
            )
        else:
            print("some error happen")   

    #     return {
    #     "msg":"draft apporoved sucessfully",
    #     "draft.id" :draft.id,
    #     "status":draft.status
    # }
    finally:
        db.close()


@approve_router.post("/draft/{id}/reject")

def reject_draft(id:int):
    db = sessionLocal()

    try:
        draft = db.query(Draft).filter(Draft.id == id).first()

        if not draft:
            raise HTTPException (status_code=404 , detail="draft not found")
        
        if draft.status == "rejected":
            return {"msg":"draft is rejected"}
        
        draft.status = "rejected"

        db.commit()

        return {
            "msg":"draft is rejected",
            "draft.id":draft.id,
            "status":"rejected"
        }
    finally:
        db.close()
        
    


