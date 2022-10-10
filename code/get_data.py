import urequests

def get_time(endpoint):
    
    w=urequests.get(endpoint)
    response = w.text
    
    return response