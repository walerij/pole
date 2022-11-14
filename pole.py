from game import game
print("Здравствуйте, друзья! В эфире программа 'Поле чудес'")

quest = game().quest
answer = game().answer
print("Загаданное слово ",game().answer)

a=input ("Введите Вашу букву:")

print(game().check_answer(a))
print(game().answer)