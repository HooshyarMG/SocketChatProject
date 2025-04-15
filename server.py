import socket
import threading

HOST = '127.0.0.1'
PORT = 5050

clients = []

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.sendall(message.encode())
            except:
                clients.remove(client)
                client.close()

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)

    try:
        while True:
            message = conn.recv(1024).decode()
            if not message:
                break

            if message.strip().lower() == "exit/":
                break

            print(f"[{addr}] says: {message}")
            broadcast(f"[{addr}] says: {message}", conn)
    except:
        print(f"[ERROR] Problem with {addr}")
    finally:
        print(f"[DISCONNECTED] {addr} disconnected.")
        clients.remove(conn)
        conn.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
