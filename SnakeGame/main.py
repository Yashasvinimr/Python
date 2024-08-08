from tkinter import *


def converter():
    miles=int(input.get())
    kilometer=miles*1.609
    new_label['text']=kilometer

window=Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


input=Entry(width=7)
input.grid(row =0, column =1)


label_1=Label(text="Miles")
label_1.grid(row=0, column=2)

label_2=Label(text="is equal to")
label_2.grid(row=1, column=0)

new_label=Label(text='0')
new_label.grid(row=1, column=1)


label_3=Label(text="km")
label_3.grid(row=1, column=2)

my_button=Button(text="Calculate", command=converter)
my_button.grid(row=2, column=1)

window.mainloop()