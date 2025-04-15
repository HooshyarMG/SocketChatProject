import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5050

class ClientGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("📨 Chat App")
        self.master.geometry("500x400")

        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', font=("Consolas", 11))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.input_field = tk.Entry(master, font=("Consolas", 12))
        self.input_field.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.input_field.bind("<Return>", self.send_message)

        self.username = simpledialog.askstring("Username", "Enter your username", parent=self.master)
        if not self.username:
            self.master.destroy()
            return

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
        self.client_socket.sendall(self.username.encode())

        self.is_connected = True
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self, event=None):
        if not self.is_connected:
            return

        message = self.input_field.get().strip()
        if message:
            self.client_socket.sendall(message.encode())
            self.input_field.delete(0, tk.END)

            if message.lower() == "/exit":
                self.is_connected = False
                self.master.quit()

    def receive_messages(self):
        while self.is_connected:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break

                self.chat_area.configure(state='normal')
                if message.startswith("🔔") or message.startswith("❌") or message.startswith("👥"):
                    self.chat_area.insert(tk.END, message + "\n", "system")
                elif message.startswith("[PM"):
                    self.chat_area.insert(tk.END, message + "\n", "pm")
                else:
                    self.chat_area.insert(tk.END, message + "\n")

                self.chat_area.configure(state='disabled')
                self.chat_area.yview(tk.END)
            except:
                break

        self.is_connected = False
        self.client_socket.close()

def run_client():
    root = tk.Tk()
    gui = ClientGUI(root)

    # رنگ‌بندی پیام‌ها
    gui.chat_area.tag_config("system", foreground="gray")
    gui.chat_area.tag_config("pm", foreground="purple")

    root.mainloop()

if __name__ == "__main__":
    run_client()
