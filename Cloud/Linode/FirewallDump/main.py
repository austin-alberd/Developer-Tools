import os
import requests
import json

#Get API Key from System Environment Variables
global API_KEY
API_KEY = os.environ["LINODE_API_KEY"]

#Global Vars To Store Stuff
global linodeID
global fireWallData


#functions to do things



programIsRun = True
while programIsRun:
    print("LINODE FW DUMP")
    print("SELECT AN OPTION TO BEGIN \n")
    print("1) SET LINODE ID \n2) PULL FIREWALL DATA \n3) EXIT")
    choice = int(input("Select a Choice: "))

    if choice == 1:
        linodeID = input("Input the ID of your linode: ")
        print(f"Your set linode ID is {linodeID}.\n")

    if choice == 2:
        url = f"https://api.linode.com/v4/linode/instances/{linodeID}/firewalls?page=1&page_size=100"

        headers = {
            "accept": "application/json",
            "authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(url, headers=headers)

        print(response.text)

        parsed = json.loads(response.text)

        print(parsed)

    if choice == 3:
        programIsRun = False

    else:
        print("Please Select A Valid Option")