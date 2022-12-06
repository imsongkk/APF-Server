import socket
import sys


def initServerSocket() -> socket:
    HOST = '0.0.0.0'
    PORT = 5000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    return server_socket


def initUnitySocket() -> socket:
    HOST = '0.0.0.0'
    PORT = 22222
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    return server_socket


if __name__ == '__main__':
    unity_socket = initUnitySocket()
    unity_socket.listen()
    unity_socket, addr = unity_socket.accept()
    print('unity connected')
    server_socket = initServerSocket()
    server_socket.listen()
    colab_socket, addr = server_socket.accept()
    print('colab connected')
    while True:
        data = colab_socket.recv(1017)  # 소켓에서 1024 byte 만큼 가져옴
        if not data:
            break
        # pose detection 받아옴
        try:
            unity_socket.sendall(data)
        except socket.error as e:
            print("error while sending :: " + str(e))

            # quit the script if connection fails (e.g. Unity server side quits suddenly)
            sys.exit()
        print('Received from', addr, data.decode())
