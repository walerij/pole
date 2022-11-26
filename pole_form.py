from tkinter import *
from tkinter import ttk


form = Tk()
form.geometry("700x500")
form.title("Поле чудес")

fr_word = Frame(form)
fr_word.grid(row=0, column=1)
fr_button = Frame(form)
fr_button.grid(row=1, column=1)
la_word= Label(fr_word, bg="orange", width=100, height=2,text="слово")
la_word.pack(side=LEFT)
def click_button():
    la_word["text"]=btn.cget('text')
for r in range(3):
    for c in range(3):
        btn = ttk.Button(fr_button, text=f"({r}{c})",command=click_button)
        btn.grid(row=r,column=c)
#la_button= Label(fr_button, bg="green", width=100, height=20,text="буквы")
#la_button.pack(side=LEFT)

form.mainloop()