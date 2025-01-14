#!/bin/env python3

# libraries
import requests

# projet files
from modules import checkConnectivity
from modules import getSession
from modules import getLogin
from modules import getCreds


def main():

    checkConnectivity()
    # start session
    session = requests.Session()

    # get the ID cookie
    id, inputs = getSession(session)
    if id == None:
        print("Error : Cannot get Session ID")
        return 1

    if inputs == {}:
        print("Error : Failed to get Session inputs")
        return 1

    # user creds
    creds = getCreds();
    if creds == None:
        return 1

    # login to myges
    getLogin(session, creds, inputs, id)

    # get course file
    # getCourseFiles(session, 

    return 0

#---------------------------------------

if __name__ == "__main__":
    main()

