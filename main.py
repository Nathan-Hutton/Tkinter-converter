from tkinter import *

#Window

window = Tk()
window.title("My Window")
window.minsize(500, 300)
window.config(padx=20, pady=20)

#Label

label = Label(text="My Lable", font=['Arial', 24, 'normal'])
label.grid(column=0, row=0)
label.config(padx=30)

#Button

def button_clicked():
    label.config(text=user_input.get())


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="No, click me", command=button_clicked)
button2.grid(column=3, row=0)

#Input

user_input = Entry(width=40)
user_input.insert(END, string="Example")
user_input.grid(column=4, row=2)

window.mainloop()
