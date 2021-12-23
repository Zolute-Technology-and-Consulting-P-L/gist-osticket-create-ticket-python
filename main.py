import requests

def createTicket(name,email,title,message,topicid):
    url = "[SUPPORTURL]/api/tickets.json"
    key = "YOUR-SECRET-KEY"

    
    data = {"name":name,
    "email":email,
    "subject":title,
    "message":message,
    "topicId":topicid,
    "autorepsond":True}
    
    headers = {
        "Accept":"application/json",
        "X-API-KEY":key

    }
    r = requests.post(url=url,json=data,headers=headers)
    if (r.status_code < 200 or r.status_code >= 300):
        return False
    
    response = r.json()
    return True
