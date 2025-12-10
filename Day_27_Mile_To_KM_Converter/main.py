from tkinter import *

def calculate():
    miles = float(text_box.get())
    km = round(miles * 1.609344, 2)
    label_result.config(text=km)

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

text_box = Entry(width=10)
text_box.insert(index=0, string="0")
text_box.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_is_equal = Label(text="is equal to")
label_is_equal.grid(row=1, column=0)

label_result = Label(text="0")
label_result.grid(row=1, column=1)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(row=2, column=1)

window.mainloop()