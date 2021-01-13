import requests

keyfile = open("key", "r")
key = keyfile.read().strip()

session = requests.Session()
session.headers = {"X-Apikey": key}

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
    except requests.exceptions.RequestException as e:
        print(e)
    except:
        print("MD5 not found for: " + ioc.strip())
