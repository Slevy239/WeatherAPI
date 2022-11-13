import zmq, json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")

#  Do 10 requests, waiting each time for a response
for request in range(1):
    print("Sending request…")
    req = ["us", "Reuters"]
    req_json = json.dumps(req)
    socket.send_json(req_json)

    #  Get the reply.
    message = socket.recv_json()
    print("%s" % message)