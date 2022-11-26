from game import game
import random
print("Здравствуйте, друзья! В эфире программа 'Поле чудес'")

game=game()
quest = game.quest
#slovo = len(quest)+3 #создание цикла - длина слова + 3 попытки

answer = game.answer
print("Загаданное слово ",answer)

while game.win=="":
    x=random.randint(0,len(game.baraban)-1)
    game.baraban_result = game.baraban[x]
    game.check_baraban()
    print("У вас на барабане выпало: ", game.baraban_result)
    print("Количество оставшихся шагов:",game.steps,game.win)
    a=input ("Введите Вашу букву:")

    if a=="слово": #если мы хотим назвать слово
        break      #прерываем цикл
    #print(game.check_answer(a))
    elif game.check_answer(a)==0:
        print ("Такой буквы нет в этом слове")

    else:
        if type(game.baraban[x]) == int:
            game.score+=game.baraban[x]
        print ("Такая буква есть в этом слове") 

    answer = game.answer
    print(answer)
def get_win(quest):
    if game.win=="":
        word=input("Назовите слово целиком:")
        print(" Ваш счет за игру : ",game.score)
        if (word==quest):
            print("Верно! Загаданное слово: ",quest,". Вы набрали ",game.score," очков.")
        else:
            print("Увы нет. Загаданное слово:",quest,"Вы проиграли. Не расстраивайтесь!")

    elif game.win == "gamer": #если победил игрок
        print("Верно! Загаданное слово: ",quest,". Вы набрали ",game.score," очков. Поздравляю с победой")

    elif game.win == "comp":
        print("Вы не угадали слово. Это ",quest,". Не расстраивайтесь")

get_win(quest)
