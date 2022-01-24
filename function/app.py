import requests

def lambda_handler(event, context, city="Porto Alegre"):

    api_key = "868a26a88dcad371f4205a319f26be8c"

    url = "http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid="+ api_key

    json_data = requests.get(url).json()

    return f"Current Temperature for {city} is {json_data['main']['temp']/10}"