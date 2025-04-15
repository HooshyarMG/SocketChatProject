import socket

HOST = '127.0.0.1'  # localhost
PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server is listening on port {PORT}...")

conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

message = conn.recv(1024).decode()
print(f"Received from client: {message}")

conn.sendall("Hello Client!".encode())

conn.close()
server_socket.close()
