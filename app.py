import os
import flask
import flask_socketio
import flask_sqlalchemy
import requests
import psycopg2

app = flask.Flask(__name__)

import models
socketio = flask_socketio.SocketIO(app)
all_numbers = []
def chatbot(vari):
    vari
    if(vari=="!!hello"):
        all_numbers.append("Hi i'm chatbot how are you?")
    elif(vari=="!!about"):
            all_numbers.append("This is a chat room created by Nathan Levis")
    elif(vari=="!!sing"):
            all_numbers.append("laydal laydal laydal!!!!!")
    elif(vari=="!!help"):
        all_numbers.append("Chatbot have a couple of commands: ")
        all_numbers.append("User !! before all of these")
        all_numbers.append("say, hello, about, tweet, sing")
    elif(vari=="!!say"):
        all_numbers.append("")
    elif(vari=="!!tweet"):
        all_numbers.append("")
    elif(vari=="connected"):
        all_numbers.append("A user has joined the chat.")
    elif(vari=="disconnected"):
       all_numbers.append("A user has left the chat.") 
    elif(vari==""):
        all_numbers.append("")
    socketio.emit('all numbers', {
        'numbers': all_numbers
    })

@app.route('/')
def hello():
    chatbot("hello")
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print 'Someone connected!'
    chatbot("connected")


@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'
    chatbot("disconnected")

@socketio.on('new number')
def on_new_number(data):
    # print 'Got a new message with data: ', data
    
    response = requests.get('https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
    json = response.json()
    
    all_numbers.append(data['number'])
    
    socketio.emit('all numbers', {
        'numbers': all_numbers
    })
    chatbot(data['number'])
    # message = models.Message(data['number'])
    # models.db.session.add(message)
    # models.db.session.commit()
    
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )