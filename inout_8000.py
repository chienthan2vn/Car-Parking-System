import socket
import time

IP = "192.168.213.103"
PORT = 8000
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"
print(IP)
def main():
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")

    """ Server has accepted the connection from the client. """
    sever, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    while True: 
        """ Receiving the filename from the client. """
        data = sever.recv(19).decode('utf-8', 'ignore')
        print(data)
        with open("./trans/check.txt", mode='w') as f:
            f.write(data)
        
if __name__ == "__main__":
    main()
