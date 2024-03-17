import socket

IP = "127.0.0.1"
PORT = 8080

sock = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM  # ipv4 connection
)  # UDP protocal

sock.bind((IP, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print(data)
