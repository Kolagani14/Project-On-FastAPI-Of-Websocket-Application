# FastAPI WebSocket Project with Frontend

This project is a real-time web application built using **FastAPI WebSockets** and a simple **frontend (HTML, CSS, JavaScript)** to demonstrate live communication between client and server.
It goes beyond basic REST APIs and shows how to handle **bi-directional communication**, where both client and server can send and receive data instantly without repeated HTTP requests.
---

## 🚀 Overview

This project focuses on building a real-time system (like a chat app) where:
* Clients connect to the server using WebSockets
* Messages are sent instantly without refreshing the page
* Multiple users can communicate in real time
This is the foundation for applications like chat systems, live notifications, and multiplayer apps.
---

## ⚙️ Features
* Real-time communication using WebSockets
* Multiple client connections handling
* Live message broadcasting
* Simple frontend interface for interaction
* FastAPI backend with async support
* No page reload required
---

## 🛠️ Tech Stack
* **Backend**: FastAPI (WebSockets)
* **Language**: Python
* **Frontend**: HTML, CSS, JavaScript
* **Server**: Uvicorn
---

## 🔌 How It Works

1. Client opens the frontend page
2. Frontend establishes a WebSocket connection to the server
3. Messages are sent through the WebSocket
4. Server receives and broadcasts messages to all connected clients
---

## 📌 WebSocket Endpoint

| Endpoint | Description              |
| -------- | ------------------------ |
| /ws      | WebSocket connection URL |

---

## ▶️ How to Run

1. Run the server:

   ```
   uvicorn main:app --reload
   ```
2. Open in browser:

   ```
   http://127.0.0.1:8000/static/index.html
   ```
---

## 🧠 What This Project Teaches

Most developers only know REST APIs, but real-world apps require real-time communication.
This project helps you understand:

* Difference between HTTP and WebSockets
* Handling multiple client connections
* Async programming in FastAPI
* Frontend-backend real-time integration
---

## 📈 Future Improvements

* Add user authentication
* Store chat messages in a database
* Add private messaging (rooms)
* Improve UI with frameworks (React/Vue)
* Deploy using WebSocket-supported hosting
---

## 💥 Reality Check

WebSockets are powerful, but:
* They are harder to scale than REST APIs
* Require proper connection management
* Can break easily if not handled correctly
If you don’t understand async behavior, this will confuse you fast.

---

## 📎 Conclusion

This project demonstrates how to build a real-time application using FastAPI WebSockets with a frontend interface. It is a strong step toward building advanced applications like chat systems, live dashboards, and collaborative tools.
