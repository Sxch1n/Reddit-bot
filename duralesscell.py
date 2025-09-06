import praw
import config
import time
import os
import requests

def bot_login():
    i=praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "duralesscell bot")
    print("loggedin")
    return i
def run_bot(i):
    for comment in i.subreddit('namesake2').comments(limit=10):
        if "!joke" in comment.body and comment.id not in users:
                #comment.reply("Batkery(https://tenor.com/view/speech-bubble-said-discord-duracell-cola-said-duracell-cola-speech-bubble-gif-12202724375420616197)")
                joke = "Here's a joke"
                joke += "\n" + requests.get("https://api.chucknorris.io/jokes/random").json()['value']
                comment.reply(joke)
                print ("replied")
                users.append(comment.id)
                with open ("users.txt" , "a") as f:
                    f.write(comment.id +"\n")

        #print(users)
        time.sleep(5)
def saved_comments():
    if not os.path.isfile("users.txt"):
        users=[]
    else:
        with open ("users.txt" , "r") as f:
            users=f.read()
            users=users.split("\n")
    return users


i=bot_login()
users=saved_comments()
print (users)
while 1:
    run_bot(i)
