import requests, json

def get_api_zipcode(country, news_outlet):


    lat = 40.045181
    long = -75.441208

    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid=53d9a1ecd2f18487b98ef685ba69b07d"
    req = requests.get(url)
    req = req.json()
    values = req["list"]
    humid = ""

    # print(values[8]["main"]["humidity"])
    i = 1
    for idx, value in enumerate(values):
        if value["main"]["humidity"]:
            humid = value["main"]["humidity"]



    res = [humid]
    jsonRes = json.dumps(res)
    # print(jsonRes)

    return jsonRes


    
    
print(get_api_zipcode("us", "CNN"))