import requests

def lambda_handler(event, context):
    
    try:
        city = str(event['pathParameters']['city'])
    except:
        city = "Porto Alegre"
    
    api_key = "868a26a88dcad371f4205a319f26be8c-io"

    url = "http://api.openweathermap.org/data/2.5/weather?q="+ str(city) +"&appid="+ api_key

    json_data = requests.get(url).json()
    
    event = f"Current Temperature for {str(city)} is {json_data['main']['temp']/10}"
    
    return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": None,
            "body": event
            }