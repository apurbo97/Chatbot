from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
os.system('color 3f')
import win32com.client as wincl
speak = wincl.Dispatch('SAPI.SpVoice')
#import speech_recognition as sr
bot = ChatBot('Bot')
def train():
	trainer = ListTrainer(bot)
	for files in os.listdir('C:/codes/Python/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
		data = open('C:/codes/Python/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
		trainer.train(data)
	messages.insert(INSERT, 'Traning Compleated!!')
	speak.Speak("Traning Compleate!!")

##def listin_user():
##	r = sr.Recognizer()
##	with sr.Microphone() as source:
##		text = "Speak Anithing..."
##		#input_user.config(text=text)
##		audio = r.listen(source)
##		# input_user.config(text="Recognizer wait....")
##	try:
##		input_user.config(text=r.recognize_google(audio))
##	except:
##		speak.Speak("Sorry could not recognize your voice")


def Enter_pressed(event):
    input_get = input_field.get()
    messages.insert(INSERT, 'You: %s\n' % input_get)
    input_user.set('')
    # speak.Speak(input_get)
    if input_get.strip() != "Bye":
    	count = 0
    	def rply():
    		reply = bot.get_response("- - "+input_get)
    		if reply == "categories:" or reply == input_get:
    			for i in range(5):
    				rply()
    				if reply != "categories:" or reply != input_get:
    					break
    		elif reply != "categories:" or reply != input_get:
    			messages.insert(INSERT, 'Bot: %s\n' % reply)
    			speak.Speak(reply)
    		elif reply == "categories:" or reply == input_get:
    			messages.insert(INSERT, 'Bot: ehh.. i dont get it!!')
    			speak.Speak('ehh.. i dont get it!!')
    			
    	rply()
    if input_get.strip() == "Bye":
    	print("Bot: Bye Bye!!...")
    	speak.Speak("Bye Bye!!...")
    return "break"


        


def enter():

    input_get = input_field.get()
    messages.insert(INSERT, 'You: %s\n' % input_get)
    input_user.set('')
    # speak.Speak(input_get)
    if input_get.strip() != "Bye":
        count = 0
        def rply():
            reply = bot.get_response("- - "+input_get)
            if reply == "categories:" or reply == input_get:
                for i in range(5):
                    rply()
                    if reply != "categories:" or reply != input_get:
                        break
            elif reply != "categories:" or reply != input_get:
                messages.insert(INSERT, 'Bot: %s\n' % reply)
                speak.Speak(reply)
            elif reply == "categories:" or reply == input_get:
                messages.insert(INSERT, 'Bot: ehh.. i dont get it!!')
                speak.Speak('ehh.. i dont get it!!')
                
        rply()
    if input_get.strip() == "Bye":
        print("Bot: Bye Bye!!...")
        speak.Speak("Bye Bye!!...")
    return "break"

window = Tk()
window.resizable(width=FALSE, height=FALSE)

scroll = Scrollbar(window)
scroll.pack(side=RIGHT,fill=Y)

messages = Text(window, width="50",bd=0, bg="#393e4f",fg ='#f4f4f4',font="Calibri",border =0,yscrollcommand=scroll.set)
messages.pack()
scroll.config(command=messages.yview)
input_user = StringVar()
input_field = Entry(window, text=input_user,fg ='#4e4e4e',bg="#f0f0f0",border=0)
button_trn = Button(window, text ='Train Bot', fg ='#f4f4f4',bg="#6f7999",width="10",command=train )
#button_mic = Button(window, text ='mic', fg ='#f4f4f4',bg="#6f7999",width="10",command=listin_user )
button_ask = Button(window, text ='ask!', fg ='#f4f4f4',bg="#6f7999",width="10",command=enter )
button_trn.pack( side = RIGHT, fill = Y )
button_ask.pack( side = RIGHT, fill = Y )
#button_mic.pack( side = RIGHT, fill = Y )
input_field.pack(side=BOTTOM, fill = BOTH)



frame = Frame(window )#, width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()
