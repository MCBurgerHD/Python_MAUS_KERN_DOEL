from tkinter import *

def button_clicked():
    label.configure(text = 'Bier!!')

fenster = Tk()
fenster.title('My first GUI with Button')
fenster.geometry('300x150')

label = Label(fenster, text = 'Hallo Welt', font = ('Arial', 20, 'bold'), fg = 'red')
button = Button(fenster, text = 'Klick Mich', command = button_clicked)

label.pack(padx = 20, pady = 30)
button.pack()

fenster.mainloop()
