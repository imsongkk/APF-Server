import socket
import sys


def initServerSocket() -> socket:
    HOST = '127.0.0.1'
    PORT = 5000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    return server_socket


def initUnitySocket() -> socket:
    address, port = '127.0.0.1', 19999
    try:
        # UDP가 아닌 TCP 이므로 DGRAM이 아닌 STREAM을 사용
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # TCP는 연결지향적이다.
        s.connect(address)
        print("Connected to address:", socket.gethostbyname(
            socket.gethostname()) + ":" + str(port))
        return s
    except OSError as e:
        print("Error while connecting :: %s" % e)

        # quit the script if connection fails (e.g. Unity server side quits suddenly)
        sys.exit()


if __name__ == '__main__':
    server_socket = initServerSocket()
    unity_socket = initUnitySocket()
    server_socket.listen()
    colab_socket, addr = server_socket.accept()
    print('Connected by', addr)
    while True:
        data = colab_socket.recv(1024)  # 소켓에서 1024 byte 만큼 가져옴
        if not data:
            break
        # pose detection 받아옴
        try:
            unity_socket.send(data)
        except socket.error as e:
            print("error while sending :: " + str(e))

            # quit the script if connection fails (e.g. Unity server side quits suddenly)
            sys.exit()
        print('Received from', addr, data.decode())
