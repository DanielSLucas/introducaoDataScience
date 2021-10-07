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
  database_uri='sqlite:///database.sqlite3'
)