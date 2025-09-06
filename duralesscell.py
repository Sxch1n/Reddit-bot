import praw
import config

def bot_login():
    i=praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "duralesscell bot")
    print("loggedin")
    return i
def run_bot(i):
    for comment in i.subreddit('battery').comments(limit=100):
        if "duracell" or "battery" in comment.body:
                comment.reply("Batkery(https://tenor.com/view/speech-bubble-said-discord-duracell-cola-said-duracell-cola-speech-bubble-gif-12202724375420616197)")
                print ("replied")

i=bot_login()
run_bot(i)
