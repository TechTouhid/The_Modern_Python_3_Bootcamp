from tkinter import *



# def km_to_mitter():
#     mitter = float(textvar.get()) * 1.6
#     text.insert(END, mitter)
#
#
#
#
# window = Tk()
# window.title("Python Mega coutse")
#
# textvar= StringVar()
#
# but1 = Button(window, text="Execute", command=km_to_mitter)
# ent1 = Entry(window, textvariable=textvar)
# text = Text(window, height=1, width=20)
#
#
#
#
#
#
# but1.grid(row=0, column=0)
# ent1.grid(row=0, column=1)
# text.grid(row=0, column=2)
#
# window.mainloop()


# 107 coding exercise 7 create a multi-widget gui

def one_to_many():
    print(value.get())

    txt_Kg.insert(END, float(value.get()) * 1000)
    txt_Pound.insert(END, float(value.get() * 2.20462))
    txt_Ounce.insert(END, float(value.get() * 35.274))

window =Tk()
window.title("Converts kg to gram, pound, ounce")


value = IntVar()
lbl1 = Label(window, text="KG")
ent1 = Entry(window, textvariable = value)
but1 = Button(window, text="Convert", command=one_to_many)

txt_Kg = Text(window, height=1, width=20)
txt_Pound = Text(window, height=1, width=20)
txt_Ounce = Text(window, height=1, width=20)

lbl1.grid(row=0, column=0)
ent1.grid(row=0, column=1)
but1.grid(row=0, column=2)

txt_Kg.grid(row=1, column=0)
txt_Pound.grid(row=1, column=1)
txt_Ounce.grid(row=1, column=2)






window.mainloop()