import socket
import threading

HOST = '127.0.0.1'
PORT = 5050

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print("\n" + message)
        except:
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    print("Connected to chat. Type 'exit/' to leave.")
    while True:
        msg = input()
        if msg.lower() == "exit/":
            break
        client_socket.sendall(msg.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
