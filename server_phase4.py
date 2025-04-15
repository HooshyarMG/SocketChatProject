import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5050

clients = {}  # conn: (ip, username)

def broadcast(message, sender_conn=None):
    for conn in list(clients):
        if conn != sender_conn:
            try:
                conn.sendall(message.encode())
            except:
                conn.close()
                del clients[conn]

def handle_client(conn, addr):
    try:
        username = conn.recv(1024).decode().strip()
        clients[conn] = (addr[0], username)
        print(f"[JOIN] {username} ({addr[0]}) joined the chat.")
        broadcast(f"🔔 {username} joined the chat.")

        while True:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            timestamp = datetime.now().strftime('%H:%M')

            if msg.lower() == "/exit":
                break
            elif msg.lower() == "/who":
                users = "\n".join([f"{u[1]} ({u[0]})" for u in clients.values()])
                conn.sendall(f"👥 Online users:\n{users}".encode())
            elif msg.lower().startswith("/pm"):
                parts = msg.split()
                if len(parts) < 3:
                    conn.sendall("❌ Invalid PM format. Use: /pm <ip> <message>".encode())
                    continue
                _, target_ip, *pm_msg_parts = parts
                pm_msg = " ".join(pm_msg_parts)
                for c, (ip, uname) in clients.items():
                    if ip == target_ip:
                        c.sendall(f"[PM from {username} at {timestamp}]: {pm_msg}".encode())
                        conn.sendall(f"[PM to {uname}]: {pm_msg}".encode())
                        break
                else:
                    conn.sendall("❌ No user with that IP.".encode())
            else:
                broadcast(f"[{timestamp}] {username}: {msg}", sender_conn=conn)

    except Exception as e:
        print(f"[ERROR] Problem with {addr}: {e}")

    finally:
        user = clients.get(conn, ("UnknownIP", "UnknownUser"))[1]
        print(f"[LEAVE] {user} disconnected.")
        broadcast(f"❌ {user} has left the chat.")
        if conn in clients:
            del clients[conn]
        conn.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[SERVER] Chat server started on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
