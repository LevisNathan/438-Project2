import os
import flask
import flask_socketio
import flask_sqlalchemy
import requests
import psycopg2
import tweepy
from random import randint, random


app = flask.Flask(__name__)

import models
socketio = flask_socketio.SocketIO(app)
all_numbers = []
def chatbot(vari):
    #split the string here then work with tokens
    # ex = vari.split('!!')
    if(vari=="!!hello"):
        mng ="Chatbot: Hi i'm chatbot"
        all_numbers.append(mng)
        mes_to_data(mng)
    elif(vari=="!!about"):
        mng = "Chatbot: This is a chat room created by Nathan Levis"
        all_numbers.append(mng)
        mes_to_data(mng)
    elif(vari=="!!sing"):
        mng = "Chatbot: laydal laydal laydal!!!!!"
        all_numbers.append(mng)
        mes_to_data(mng)
    elif(vari=="!!help"):
        mng = "Chatbot have a couple of commands: "
        mng = "User !! before all of these"
        mng = "say, hello, about, tweet, sing"
        all_numbers.append(mng)
        mes_to_data(mng)
        all_numbers.append(mng)
        mes_to_data(mng)
        all_numbers.append(mng)
        mes_to_data(mng)
    elif(vari=="!!say"):
        va = vari.split('!!say ' , 1)
        mng = va[1]
        all_numbers.append(mng)
        mes_to_data(mng)
    elif(vari=="!!tweet"):
        t =twit()
        tweety = t.text
        mng = "Chatbot: " + tweety
        all_numbers.append(mng)
        mes_to_data(mng)
    elif(vari=="connected"):
        mng = "Chatbot: A user has joined the chat."
        all_numbers.append(mng)
        mes_to_data(mng)
    elif(vari=="disconnected"):
        mng = "Chatbot: A user has left the chat."
        all_numbers.append(mng) 
        mes_to_data(mng)
    elif(vari==""):
        all_numbers.append("")
        mes_to_data(mng)
    socketio.emit('all numbers', {
        'numbers': all_numbers
    })
def mes_to_data(mng):
    message = models.Message(mng)
    models.db.session.add(message)
    models.db.session.commit()
def twit():
    consumer_key=  "qOYlXsiQhXjU5LHvF7nWokRCX"
    consumer_secret = "6wkXylgkKs4htvol2MysqJRhzZ900OqYMPhYlLeVJxux4joyWq"
    access_token = "322795723-rYG4Pe1zKl7W245ASt1Pm6dRpVxKyDFX04MOjalv"
    access_token_secret = "qUG4DmGu7TrBam9baVgYdtxS7wGRMASpgqSuFIHkVpUBs"
    callback_url=""
    
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    
    api = tweepy.API(auth)
    #getting tweets and making sure they are only in english
    public_tweets = tweepy.Cursor(api.search, q="Music -RT", lang = "en").items(50)
    
    randTweet=sorted(public_tweets, key=lambda x:random())
    a = randint(0,50)
    t = randTweet[a]
    return t
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
    mes = json['name']+": " + data['number']
    all_numbers.append(mes)
    
    socketio.emit('all numbers', {
        'numbers': all_numbers
    })
    chatbot(data['number'])
    mes_to_data(mes)
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )