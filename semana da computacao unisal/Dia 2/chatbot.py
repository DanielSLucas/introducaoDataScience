#!/usr/bin/env python
# coding: utf-8

import glob
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from tkinter import *          
from random import choice

arquivos_treino = [f for f in glob.glob("dados_treino/*.yml")]
# print(arquivos_treino) # listar nomes dos arquivos de treinamento

# criação de uma instancia do chatbot
bot_unisal = ChatBot(
  'Chatbot',
  storage_adapter='chatterbot.storage.SQLStorageAdapter',
  database_uri='sqlite:///chatbotDB.sqlite3'
)

# treinando o chatbot com os arquivos de treino
# salva também todo o treino no banco de dados
treino = ChatterBotCorpusTrainer(bot_unisal)
for arq in arquivos_treino:
  treino.train(arq)
# treino.train("chatterbot.corpus.portuguese") #treinar com a base de dados do chatterbot

def converse():
  pergunta = ''
  while pergunta != 'sair':
    pergunta = input()
    resposta = bot_unisal.get_response(pergunta)
    if float(resposta.confidence) > 0.1:
      print(resposta)      
    else:
      print('Não entendi')

converse()

# ====== contrução da interface com o tkinter =============
# root = Tk() # intancia do tk
# root.minsize(width=100, height=100) # tamanho da tela
# root.geometry('300x320+0+0')
# user = StringVar() # variaveis de entrada                          
# bot  = StringVar() # respostas do bot   
# Label(root, text=" Chatbot ").pack()
# Label(root, text="     ").pack()
# Label(root, text="     ").pack()             
# root.title(" ChatBot ") # titulo do chatbot    
# Label(root, text=" Digite sua mensagem: ").pack()
# Entry(root, textvariable=user,width="50").pack()          
# Label(root, text=" Bot: ").pack()                
# Entry(root, textvariable=bot,width="50").pack()      

# # Display da interface criada
# def main():
#     pergunta = user.get()
#     resposta = bot_unisal.get_response(pergunta)
#     if float(resposta.confidence) > 0.1:
#         resp = []
#         resp.append(resposta)
#         bot.set(choice(resp))
#     else:
#         resposta = ['Não entendi']
#         bot.set(choice(resposta))                        
# Label(root, text="     ").pack()
# Button(root, text="Enviar", command=main).pack()        
                
# mainloop()

# ======== TREINAR MANUALMENTE ===========
# trainer = ListTrainer(bot_unisal)

# trainer.train([
#   'Qual o seu nome?',
#   'Bob, pode me chamar de bob',
#   'Conhece o Fernando?',
#   'Aquele chupe engole? Claro que conheço',
#   'Sabe quem é o amor da minha vida?'
#   'Gabriella Helena Averaldo dos Santos, correto?'
#   'Sim!!Corretissimo'
#   'Alias quando vai pedir ela em casamento?'
# ])

# trainer.train([
#   'Sabe quem e o amor da minha vida?'
#   'Gabriella Helena Averaldo dos Santos'
#   'Sim!!Corretissimo'
#   'Alias quando vai pedir ela em casamento?'
# ])

# trainer.train([
#   'sair'
#   'Okay byee'
# ])

