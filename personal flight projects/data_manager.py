import requests
from pprint import pprint
import html

sheety_api = "https://api.sheety.co/a8fa40741c590e518b0f8d43b99377d7/ownCopy/prices"

class Datamanager:
    def __init__(self) -> None:
        self.data = {}
    
    #This class is responsible for talking to the Google Sheet.
    def destination_data(self):
        response = requests.get(url=sheety_api)
        data = response.json()
        self.data = data["prices"]
        return self.data
    
    def putrequest(self,sheet_data):
        for city in sheet_data:
            new_data={
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(url=f"https://api.sheety.co/a8fa40741c590e518b0f8d43b99377d7/ownCopy/prices/{city['id']}",json=new_data)
            