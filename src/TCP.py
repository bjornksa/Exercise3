import socket
from time import sleep

with open("src/server_ip.txt") as ip:
    TCP_IP = ip.readline()
TCP_PORT = 34933

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
data = sock.recv(1024)
print(data)


sock.send(b"Connect to: 10.100.23.147:34933\0")

for i in range(5):
    send_data = b"YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoooo"*(2*i+1) + b"\0"
    print("sending: ", send_data)
    sock.send(send_data)
    print("...sent")

    print("receiving...")
    data = sock.recv(1024)

    print(data)
    print(i, "\n")

sock.close()