import requests
from  datetime import datetime

user_name = "puneeth"
token = "Dcet@2022"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"



user_params = {
    "token":token,
    "username":user_name,
    "agreeTermsOfService":"yes",
    "notMinor" : "yes",
}

#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)

graph_config={
    "id":"graph1",
    "name" : "coding graph",
    "unit":"hours",
    "type" : "float",
    "color" : "shibafu",
}

header ={
    "X-USER-TOKEN":token
}

#response = requests.post(url=graph_endpoint,json=graph_config,headers=header)
#print(response.text)

graph_id = graph_config["id"]
pixela_creation_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph_id}"

today = datetime(year=2023,month=9,day=22)
date= today.strftime("%Y%m%d")

pixela_data = {
    "date" : date ,
    "quantity" : "9.8" ,
}

#response = requests.post(url=pixela_creation_endpoint,json=pixela_data,headers=header)
#print(response.text)

pixela_update_endpoint = f"{pixela_creation_endpoint}/{date}"

new_pixela_data = {
    "quantity":"2.2"
}

#response = requests.put(url=pixela_update_endpoint,headers=header,json=new_pixela_data)
#print(response.text)

delete_endpoint = f"{pixela_update_endpoint}"

response = requests.delete(url=delete_endpoint,headers=header)
print(response.text)
