import socket

HOST = "127.0.0.1"
PORT = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    data = input("입력 : ")
    client_socket.sendall(data.encode())

client_socket.close()
