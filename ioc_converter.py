import requests

session = requests.Session()
session.headers = {"X-Apikey": "Your VT Api Key"}


ioc_list = open("ioc_list.txt", "r")
IoC = ioc_list.readlines()


for ioc in IoC:
    url = "https://www.virustotal.com/api/v3/files/" + ioc.strip()
    try:
        response = session.get(url)
        jsonResponse = response.json()
        print(
            "The MD5 of "
            + ioc.strip()
            + " is: "
            + jsonResponse["data"]["attributes"]["md5"]
        )
    except:
        print("MD5 not found for: " + ioc.strip())
