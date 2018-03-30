# -*- coding: utf-8 -*-

#import libs
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

#testando bot
bot = ChatBot('Test')

#criando list de conversação, tomando base na pergunta e resposta seguinte
#validar ordem crescente
convSaudacao = ['Oi', 'Olá','Qual é o seu nome?', 'Bom dia, como vai?', 'Estou bem, obrigada por pergutar']

#criando list de conversação 2, abrangendo o foco
convMusic = ['Você gosta de músicas?', 'Sim, e você?', 'Adoro!', 'Qual seu estilo de música favorito?','Rock!','Que Legal!']

#metodo de treinamento
bot.set_trainer(ListTrainer)

#treino
bot.train(convSaudacao)
bot.train(convMusic)

#laço de perguntas
while True:
    quest = input('You: ')
    response = bot.get_response(quest)
    
    print ('Bot: ' ,response)