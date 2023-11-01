#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import Datamanager
from flight_search import FlightSearch

city1 = FlightSearch.search("London")
from_date = "10/10/2023"
to_date =  "11/10/2023"

Data = Datamanager()
sheet_data = Data.destination_data()


for city in sheet_data:
    city["iataCode"] = FlightSearch.search(city=city["city"])

Data.putrequest(sheet_data=sheet_data)
FlightSearch.Routeserach(city=city1,from_date=from_date,to_date=to_date)