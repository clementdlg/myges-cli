# libs
import requests
from bs4 import BeautifulSoup       # getSession()

# project files
from .utils import setHeaderUserAgent
from .utils import checkReturnVal
from .utils import getEnv

def getLogin(session, creds, inputs, id):

    url = "https://ges-cas.kordis.fr/login"

    headers = setHeaderUserAgent()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Cookie"] = "JSESSIONID=" + str(id)

    # params
    params = {
        "service" : "https://myges.fr/j_spring_cas_security_check"
    }

    data = {
        "username": creds["user"],
        "password": creds["password"],
        "lt": inputs["lt"],
        "execution": inputs["execution"],
        "_eventId": "submit",
        "submit": "CONNEXION"
    }

    response = requests.post(url, headers=headers, data=data, params=params, allow_redirects=True)
    checkReturnVal(response.status_code, "login", 200)

    print(response.text)
    return

#---------------------------------------
def getCreds():
    creds = dict()

    user = getEnv("MYGES_USER")
    if user == None:
        print("Error : Unset environment variable MYGES_USER")
        return

    password = getEnv("MYGES_PASSWORD")
    if password == None:
        print("Error : Unset environment variable MYGES_PASSWORD")
        return

    creds["user"] = user
    creds["password"] = password

    return creds

#---------------------------------------

def getSession(session):
    url = "https://myges.fr/open-session"
    inputs = dict()

    # set the header
    headers = setHeaderUserAgent()

    # send request
    response = session.get(url, headers=headers)

    checkReturnVal(response.status_code, url, 200)

    # get the ID cookie
    id = None
    for cookie in session.cookies:
        if cookie.name == "JSESSIONID":
            id = cookie.value

    # parse html
    soup = BeautifulSoup(response.text, 'html.parser')
    # get the "<input type='hidden" fields
    hidden = soup.find_all('input', {'type': 'hidden'})

    # retrieve values
    for tag in hidden:
        name = tag.get('name')
        value = tag.get('value')
        inputs[name] = value

    return (id, inputs)

