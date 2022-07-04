from flask import Blueprint, redirect, render_template, request, url_for, session
from flask_login import current_user, login_required
from flask_socketio import join_room, leave_room, send, emit, disconnect
from . import socketio


chat = Blueprint('chat', __name__)


@chat.route('/join', methods=('GET', 'POST'))
@login_required
def join():
    if request.method == 'POST':
        room = request.form['name']
        return redirect(url_for('chat.chat_room', room=room))

    return render_template('join.html')


@chat.route('/chat/<room>')
@login_required
def chat_room(room):
    session['room'] = room
    return render_template('chat.html', username=current_user.username)


@socketio.on('message')
def handle_message(message):
    send(message, to=session['room'])


@socketio.on('joined')
def handle_join(data):
    room = session['room']

    emit('joined', data, to=room)
    join_room(room)


@socketio.on('left')
def handle_left(data):
    room = session['room']

    emit('left', data, to=room)
    leave_room(session['room'])

    disconnect()
