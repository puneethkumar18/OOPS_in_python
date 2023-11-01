import requests


APP_ID = "e0f091d2"
APP_KEY = "89a571e071a31cb3d3d34c8bdf69934d"

GENDER = "Male"
AGE = 21
HEIGHT_CM = 177
WEIGHT_KG = 70

Exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("tell me which exercise you did:")

headers = {
    "x-app-id":APP_ID,
    "x-app-key" : APP_KEY,

}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=Exercise_endpoint,json=parameters,headers=headers)
response.raise_for_status()
results = response.text
print(results)