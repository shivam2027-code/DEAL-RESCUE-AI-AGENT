from fastapi import APIRouter , requests , HTTPException , Query
from app.models.draft import Draft  

from app.db.database import sessionLocal


draft_router = APIRouter()
@draft_router.get("/drafts")

def get_all_drafts(status:str =Query(default=None)):
    db = sessionLocal()
    
    try:
        query = db.query(Draft)

        if status:
            query = query.filter(Draft.status == status)

        drafts = query.all()    


        result = []
        for draft in drafts:
            result.append({
                "id":draft.id,
                "reply":draft.reply,
                "status":draft.status,
                "event_id":draft.event_id
            })
        return result

    finally:
        db.close()    
    



@draft_router.get("/drafts/{id}")
def get_single_draft(id:int):
    db = sessionLocal()

    try:
        draft = db.query(Draft).filter(Draft.id == id).first()

        if not draft:
            raise HTTPException(status_code=404 , detail="draft not found")
        
        return {
            "id":draft.id,
            "reply":draft.reply,
            "status":draft.status,
            "event_id":draft.event_id
        }
    
    finally:
        db.close()



