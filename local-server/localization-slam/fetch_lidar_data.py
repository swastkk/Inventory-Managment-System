import socket

# Setup Socket
host = '192.168.0.104'  
port = 7600  
s = socket.socket()
s.bind((host, port))
s.listen(1)

conn, addr = s.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data)

conn.close()
