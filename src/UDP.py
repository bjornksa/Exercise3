import socket
import select
from time import sleep


UDP_PORT = 20006
UDP_IP = "10.100.23.147"

send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

send_sock.connect((UDP_IP, UDP_PORT))
recive_sock.bind(("", UDP_PORT))


while True:
    print("Sending 8...")
    
    
    send_sock.send(b"MESSAGE"*100)
    data, addr = recive_sock.recvfrom(1024) # buffer size is 1024 bytes


    print("received message:", data)
    sleep(0.5)

send_sock.close()
recive_sock.close()