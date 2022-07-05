# chat-app
A real-time chat app made with Flask and Socket.io.

## Features
- Authentication (Sign Up, Login and Logout).
- Rooms.
- Real-time chat with usernames, connect and disconnect messages.
- Responsive UI with Bulma.
- (To-Do) Message persistency.

## Installation
Clone the repository:
```
git clone https://github.com/kappq/chat-app.git
```
Install the requirements:
```
pip install -r requirements.txt
```
Open a Python shell and create the database:
```py
>>> from chat_app import db, create_app, models
>>> db.create_all(app=create_app())
```
Run the app:
```
flask run
```
