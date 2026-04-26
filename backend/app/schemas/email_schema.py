from pydantic import BaseModel

class EmailWebhook(BaseModel):

    email:str
    sender:str