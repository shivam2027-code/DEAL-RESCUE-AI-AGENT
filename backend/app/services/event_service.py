from app.models.email_event import Event
from app.db.database import sessionLocal , get_db



# event - email recieved 

def create_event(email:str , sender:str):
    db = sessionLocal()

    event = Event(
        email = email,
        sender = sender ,
        event_type = "email_reciedved"
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    db.close()
    
    return event.id