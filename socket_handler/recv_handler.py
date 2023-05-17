import json

def recv_handler(self, websocket, recv_data):
    cmd = recv_data['cmd']
    data = recv_data['data']

    if cmd == '1001' : # connect
        sendData = {
            cmd: 1,
            data : 'success'
        }
        websocket.send(json.dumps(sendData))