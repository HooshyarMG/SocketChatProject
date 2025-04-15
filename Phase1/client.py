import socket

HOST = '127.0.0.1'
PORT = 5050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.sendall("Hello Server!".encode())

response = client_socket.recv(1024).decode()
print(f"Response from server: {response}")

client_socket.close()
