import requests

def lambda_handler(event, context, city="Porto Alegre"):

    api_key = ""

    url = "http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid="+ api_key

    json_data = requests.get(url).json()

    return f"Current Temperature for {city} is {json_data['main']['temp']/10}"
