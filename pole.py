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

print("Загаданное слово:",quest)    