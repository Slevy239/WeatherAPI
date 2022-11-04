import json, requests
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_json()
    message = json.loads(message)
    lat, long = message[0], message[1]
    print("Received request: %s" % message)

    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid=53d9a1ecd2f18487b98ef685ba69b07d"
    req = requests.get(url)
    req = req.json()
    humid = temp = ""
    vals = []
    days = []
    values = req["list"]

    for value in values:
        if value["main"]:
            # humid = value["main"]["humidity"]
            # temp = value["main"]["temp"]
            vals.append(value["main"]["humidity"])

    for i in range(len(vals)):
        if i % 8 == 0:
            days.append(vals[i])
    print(days)
    res = days
    json_res = json.dumps(res)

    socket.send_json(json_res)