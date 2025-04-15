import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"[{addr}] says: {message}")
            response = input(f"Your reply to {addr}: ")
            conn.sendall(response.encode())
        except:
            break
    print(f"[DISCONNECTED] {addr} disconnected.")
    conn.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
