import socket
import time

IP = "192.168.213.69"
PORT = 8080
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"
#Khoi tao ket noi
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(ADDR)

def main():
    while True: 
        with open("./trans/re.txt", mode='w+') as f:
            data = f.read()
            if data != "":
                server.send(str(data).encode(FORMAT))
                f.write("")
                time.sleep(3)
        
if __name__ == "__main__":
    main()
