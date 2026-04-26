
def detect_comptiter(email:str):

    competitor = ["salesforce" ,"hubspot"]
    
    email_lower = email.lower()

    for comp in competitor:
        if comp in email_lower:

            return {
                "risk_type":"competitor_mention",
                "competitor":comp.capitalize()
            }
            
    return None
    


    
