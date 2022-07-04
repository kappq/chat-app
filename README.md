# chat-app
This is a real-time chat app made with Flask and Socket.io.

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
