from tkinter import *


form = Tk()
form.geometry("1000x700")
form.title("Поле чудес")

fr_word = Frame(form)
fr_word.grid(row=0, column=1)
la_word= Label(fr_word, bg="orange", width=70, height=2,text="слово")
la_word.pack(side=LEFT)

form.mainloop()