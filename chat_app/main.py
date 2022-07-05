from flask import Blueprint, redirect, render_template, request, url_for, session
from flask_login import current_user, login_required
from flask_socketio import join_room, leave_room, send, emit, disconnect
from . import socketio, db


main = Blueprint("main", __name__)


@main.route("/", methods=("GET", "POST"))
@login_required
def index():
    if request.method == "POST":
        session["room"] = request.form["room"]
        return redirect(url_for("main.chat"))

    return render_template("index.html")


@main.route("/chat")
@login_required
def chat():
    return render_template(
        "chat.html", room=session["room"], username=current_user.username
    )


@socketio.on("message")
def handle_message(message):
    send(message, to=session["room"])


@socketio.on("joined")
def handle_join(data):
    room = session["room"]

    join_room(room)
    emit("joined", data, to=room)


@socketio.on("left")
def handle_left(data):
    room = session["room"]

    leave_room(session["room"])
    emit("left", data, to=room)
