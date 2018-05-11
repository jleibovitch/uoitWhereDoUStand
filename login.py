import requests
from bs4 import BeautifulSoup

def login(username, password):
    
    payload = {
        'user': username,
        'pass': password,
        'uuid': '0xACA021'
    }

    with requests.Session() as request_session:
        print("Logging in as %s" % payload['user'])
        request_session.post(
            'https://portal.mycampus.ca/cp/home/login', data=payload)
        detail_url = 'https://ssbp.mycampus.ca/prod_uoit/bwskogrd.P_ViewTermGrde'
        # r = request_session.get(detail_url)
        r = request_session.get(
            'https://portal.mycampus.ca/cp/ip/login?sys=sct&url=' + detail_url)
        print(r.text)
    
    return