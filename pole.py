from game import game
print("Здравствуйте, друзья! В эфире программа 'Поле чудес'")

game=game()
quest = game.quest
slovo = len(quest)+3 #создание цикла - длина слова + 3 попытки

answer = game.answer
print("Загаданное слово ",answer)

for i in range(0,slovo):
    a=input ("Введите Вашу букву:")

    print(game.check_answer(a))
    answer = game.answer
    print(answer)

word=input("Назовите слово целиком:")
if (word==quest):
    print("Верно! Загаданное слово: ",quest,". Вы выиграли АВТОМОБИЛЬ!")
else:
    print("Увы нет. Загаданное слово:",quest,"Вы проиграли. Не расстраивайтесь!")    