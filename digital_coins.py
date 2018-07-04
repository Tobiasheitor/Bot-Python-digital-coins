from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

coin_bot = ChatBot("chatbot")


coin_bot.set_trainer(ListTrainer)

coin_bot.train([
    "Hi there!",
    "Hello",
    "Oi!",
    "Hello",
])



data1 = open('data/bitcoin-data.txt').read()
data2 = open('data/bot-data.txt').read()
data3 = open('data/ether-data.txt').read()

conversations = data1.strip().split('\n')
coin_bot.train(conversations)
conversations = data2.strip().split('\n')
coin_bot.train(conversations)
conversations = data3.strip().split('\n')
coin_bot.train(conversations)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    print("ok")
    userText = request.args.get('msg')
    return str(coin_bot.get_response(userText))

if __name__ == "__main__":
    app.run()
