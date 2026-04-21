from app.db.database import sessionLocal
from app.models.draft import Draft




# def generate_draft(email: str, risk_data: dict | None):

#     if risk_data and risk_data.get("competitor"):
#         competitor = risk_data["competitor"]

#         return f"""
#         Thanks for considering multiple options.

#         Compared to {competitor}, we offer more flexibility and better customization for your needs.

#         Happy to walk you through this in detail.
#         """

#     return """
#     Thanks for your response.

#     Let me know if you have any questions or need more details.
#     """


def save_draft(reply:str , event_id:int):
    db = sessionLocal()

    draft = Draft(
        reply = reply,
        event_id = event_id
    )

    db.add(draft)
    db.commit()
    db.refresh(draft)
    print("event_id",event_id)

    db.close()