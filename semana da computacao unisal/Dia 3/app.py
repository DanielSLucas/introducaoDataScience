from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

portugues_bot = ChatBot(
  'Chatbot',
  storage_adapter='chatterbot.storage.SQLStorageAdapter',
  database_uri='sqlite:///chatbotDB.sqlite3'
)
trainer = ChatterBotCorpusTrainer(portugues_bot)
trainer.train("chatterbot.corpus.portuguese.conversations")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(portugues_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
