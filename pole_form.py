from tkinter import *
from tkinter import ttk, messagebox

from game import game #импортируем класс game


form = Tk()
form.geometry("700x500")
form.title("Поле чудес")
# создаем фреймы
fr_word = Frame(form)
fr_word.grid(row=0, column=1)
fr_button = Frame(form)
fr_button.grid(row=1, column=1)
fr_pole = Frame(form)
fr_pole.grid(row=2, column=1)

#создаем игру
game=game()
global quest
quest = game.quest
global answer 
answer= game.answer

#прогружаем слово и играем
la_word= Label(fr_word, bg="green", fg="white",font="Arial,42", width=100, height=2,text=answer)
la_word.pack()
#def click_button():
#    la_word["text"]=btn.cget('text')
#for r in range(3):
#    for c in range(3):
#        btn = ttk.Button(fr_button, text=f"({r}{c})",command=click_button)
#        btn.grid(row=r,column=c)

la_button= Label(fr_button, bg="orange", width=100, text="Количество ходов: "+str(game.steps))
la_button.pack(side=LEFT)

pole = Entry(fr_pole,fg="yellow", bg="blue", width=50,text="a", font="Tahoma,16")
pole.pack()
def pole_check():
    letter=pole.get()
    if game.check_answer(letter)==0:
        messagebox.showinfo(title="Информация", message="Буквы "+letter+" нет в этом слове!")
    elif game.check_answer(letter)==1:
        messagebox.showinfo(title="Информация", message="Буква "+letter+"! Есть такая буква в этом слове!")    
    pole["text"]=""
    answer = game.answer  
    la_button["text"]="Количество ходов: "+str(game.steps)      
    la_word["text"]=answer
    if game.win!="":
        get_win(quest)

def get_win(quest):
    if game.win == "gamer": #если победил игрок
        messagebox.showinfo(title="Информация", message="Верно! Загаданное слово: "+quest+". Поздравляю с победой")

    elif game.win == "comp":
        messagebox.showinfo(title="Информация",message="Вы не угадали слово. Это "+quest+". Не расстраивайтесь")


pole_button=Button(fr_pole,text="Назвать букву",command=pole_check)
pole_button.pack()

form.mainloop()