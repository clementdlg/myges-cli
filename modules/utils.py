import os   # getEnv()
import socket   # checkConnectivity()
import pprint   # prettify dicts

def printDict(dicti):
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
    pp.pprint(dicti)
    return

#---------------------------------------
def getEnv(variable):
    value = os.getenv(variable)
    if value:
        return value
    return

#---------------------------------------
def checkReturnVal(value, name, exp):
    if value != exp:
        print(f"Error : Request '{name}' failed with status code '{value}'. Expected {exp}")
        exit(1)
    return

#---------------------------------------
def setHeaderUserAgent():
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'

    return { 'User-Agent': userAgent }

#---------------------------------------
def checkConnectivity():
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=5)
    except socket.error:
        print("Error : No internet connection")
        exit(1)

#---------------------------------------
