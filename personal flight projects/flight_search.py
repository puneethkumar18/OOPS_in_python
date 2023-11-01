import requests


end_point = "https://api.tequila.kiwi.com"


api_key = "Z8Ili2nmBYAUhKpbXgmRcmsT2q6tFOCX"

class FlightSearch:
    def __init__(self) -> None:
        self.flyfrom 
        self.date_from
        self.date_to
    #This class is responsible for talking to the Flight Search API.
    def search(city):
        loction_point =f"{end_point}/locations/query"
        headers = {"apikey": api_key}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=loction_point,headers=headers,params=query)
        results = response.json()["locations"]
        code = results[0]['code']
        return code
    
    def Routeserach(city,from_date,to_date):
        headers ={
            "apikey":api_key
        }
        parameter={
            "fly_from":city,
            "date_from":from_date,
            "date_to":to_date
        }
        route_endpoint = f"{end_point}/search"

        response = requests.get(url=route_endpoint,params=parameter,headers=headers)
        print(response.text)
    

    