from tkinter import *

def Enter_pressed(event):
    input_get = input_field.get()
    messages.insert(INSERT, 'You: %s\n' % input_get)
    input_user.set('')
    return "break"
def enter():
    input_get = input_field.get()
    messages.insert(INSERT, 'You: %s\n' % input_get)
    input_user.set('')
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
button = Button(window, text ='ask!', fg ='#f4f4f4',bg="#6f7999",width="10",command=enter )
button.pack( side = RIGHT, fill = Y )
input_field.pack(side=BOTTOM, fill = BOTH)



frame = Frame(window )#, width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()