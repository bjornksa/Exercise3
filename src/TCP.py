import socket
from time import sleep

with open("src/server_ip.txt") as ip:
    TCP_IP = ip.readline()
TCP_PORT = 34933

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
data = sock.recv(1024)
print(data.split(b"\0")[0])


sock.send(b"Connect to: 10.100.23.147:34933\0")

for i in range(5):
    send_data = b"YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoooo\0"
    print("sending: ", send_data)
    sock.send(send_data)
    print("...sent")

    print("receiving...")
    data = sock.recv(1024)

    data = data.split(b"\0")[0]

    print(data)
    print(i, "\n")

sock.close()