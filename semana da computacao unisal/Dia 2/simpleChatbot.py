from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

trainer.train([
  "Oi",
  "Olá",
  "Tudo bem?"
])

# Get a response to the input text 'I would like to book a flight.'

response = chatbot.get_response('I would like to book a flight.')

while True:
  pergunta = input()
  resposta = resposta = chatbot.get_response(pergunta)
  print(resposta)