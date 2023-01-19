from tkinter import *

window = Tk()
window.title("My Window")
window.minsize(500, 300)

label = Label(font=['Arial', 24, 'normal'])
label.pack(side='top')


def button_clicked():
    label.config(text=user_input.get())


button = Button(text="Click me", command=button_clicked)
button.pack()

user_input = Entry(width=40)
user_input.insert(END, string="Example")
user_input.pack()

text = Text(height=5, width=20)
text.pack()
text.insert(END, "Example")


def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


def checkbox_used():
    print(check_variable.get())


check_variable = IntVar()
checkbox = Checkbutton(text="Is On", variable=check_variable, command=checkbox_used)
checkbox.pack()


def radio_button_used():
    print(radio_state.get())


radio_state = IntVar()
radio_button1 = Radiobutton(text='option1', value=1, variable=radio_state, command=radio_button_used)
radio_button2 = Radiobutton(text='option2', value=2, variable=radio_state, command=radio_button_used)

radio_button1.pack()
radio_button2.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
