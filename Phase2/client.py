import socket

HOST = '127.0.0.1'
PORT = 5050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    client_socket.sendall(msg.encode())
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

client_socket.close()
