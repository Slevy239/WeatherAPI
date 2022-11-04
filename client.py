#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq, json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(1):
    print("Sending request…")
    req = ["40.045181", "-75.441208"]
    req_json = json.dumps(req)
    socket.send_json(req_json)

    #  Get the reply.
    message = socket.recv_json()
    print("Received reply %s [ %s ]" % (request, message))