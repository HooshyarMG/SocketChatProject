# 💬 Socket Chat Project

یک پروژه برنامه نویسی سوکت کامل در پایتون که یک سیستم پیام رسانی چند مشتری را شبیه سازی می کند. این پروژه در چهار مرحله اجرا می‌شود و به تدریج قابلیت‌ های بیشتری را اضافه می‌کند: از اتصالات ساده تا چت رابط کاربری گرافیکی کامل با پیام‌ های خصوصی.

-----

## 📁 Project Structure
```
SocketChatProject/
├── phase1/
│   ├── server.py       # Simple one-client server
│   └── client.py       # One-client client
├── phase2/
│   ├── server.py       # Multi-client server with threading
│   └── client.py       # Same client
├── phase3/
│   ├── server.py       # Broadcast chat server
│   └── client.py       # Basic text-based group chat client
├── phase4/
│   ├── server_phase4.py  # Advanced server with usernames, timestamps, private messaging
│   └── client_gui.py     # Tkinter-based GUI client
├── screenshots/         # Screenshots of GUI and server
└── README.md

```
## 🧩 Phase 1 – Basic Server-Client Communication

### 🎯 Goal:

- یک ارتباط اساسی بین یک کلاینت و یک سرور برقرار کنید.

### ⚙ Structure:

- سرور روی لوکال هاست و یک پورت خاص گوش می دهد.
- کلاینت متصل می شود و "Hello Server" را ارسال می کند.
- سرور با "سلام مشتری" پاسخ می دهد.
- جداسازی تمیز.
### 🧪 Technologies:

- Python socket
- TCP/IP

### 📌 Notes:

- AF_INET and SOCK_STREAM used
- Create و Teardown سوکت اولیه



## 🧩 Phase 2 – Multi-Client Support with Threading
### 🎯 Goal:

- به چندین مشتری اجازه دهید به طور همزمان متصل شوند.

### ⚙ Structure:

- سرور هر مشتری را در یک موضوع جدید می پذیرد.
- پیام های چاپ شده به ازای هر مشتری.
### 🧪 Technologies:

- threading
- socket

### 📌 Notes:

- هر مشتری در Thread خود اجرا می شود.
- پاسخ ساده در هر پیام.


##🧩 Phase 3 – Broadcast Messaging
### 🎯 Goal: 

-از یک مشتری به سایر مشتریان پیام ارسال کنید.

### ⚙ Structure:

- سرور لیستی از مشتریان فعال را نگه می دارد.
- پیام ورودی برای همه (به جز فرستنده) پخش می شود.
### 🧪 Technologies:

- broadcast() function.
- Shared clients[] list.


### 📌 Notes:

- استفاده از exit/ برای ترک چت.
- ادد کردن Relay Mechanism.

## 🧩 Phase 4 – GUI & Private Messaging
### 🎯 Goal: 
- قابلیت استفاده را با رابط کاربری گرافیکی و ویژگی های چت پیشرفته افزایش دهید.

### ⚙ Structure:

- GUI made with tkinter.
- Username required on start.
- /pm <ip> <message> for private messages.
- /who lists connected users.
- رابط کاربری گرافیکی ساخته شده با tkinter.
- نام کاربری هنگام شروع مورد نیاز است.
- /pm <ip> <پیام> برای پیام های خصوصی.
- /who که کاربران متصل را فهرست می کند.


### 🧪 Technologies:
- tkinter, datetime
- socket, threading

### 📌 Notes:

- جت باکس GUI با ScrolledText
- چت خصوصی، تایم ستمپس و خروجی .


## 🚀 How to Run

### 1. Run the Server:
- python server_phase4.py

### 2. Run the GUI Client:
- python client_gui.py



# 🖼 Screenshots:

### First User:

![Screenshot (730)](https://github.com/user-attachments/assets/41bdf938-3f9e-46c1-968b-4ba45c419ec9)

![Screenshot (731)](https://github.com/user-attachments/assets/6c5dd596-0f5d-434e-9923-83cb83767d77)


### Second User:

![Screenshot (732)](https://github.com/user-attachments/assets/dfdfc59b-9174-4720-9161-991b78f0b5a5)



# 👨‍💻 Developer Info:
- Name: Hooshyar Moghaddam
- GitHub: https://github.com/HooshyarMG


# 🧠 Summary Table: 

| Phase   | Description                                | Technologies             |
|---------|--------------------------------------------|---------------------------|
| Phase 1 | One-to-one message exchange                | `socket`, TCP             |
| Phase 2 | Multi-client using threading               | `threading`, `socket`     |
| Phase 3 | Broadcast to all clients                   | `broadcast`, `clients[]`  |
| Phase 4 | GUI client, private chat, timestamp, `/pm` | `tkinter`, `/who`, `/pm`  |















