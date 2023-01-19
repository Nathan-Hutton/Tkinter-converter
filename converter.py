from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.insert(END, string='0')

miles_label = Label(text="Miles")

is_equal_label = Label(text="is equal to")

result_label = Label(text='0')
result_label.config(padx=30)

km_label = Label(text='Km')


def calculate():
    miles = int(mile_input.get())
    km = round(miles * 1.6, 2)
    result_label.config(text=str(km))


calculate_button = Button(text="Calculate", command=calculate)

mile_input.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
result_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)

window.mainloop()