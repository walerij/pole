import random
class game:
    def __init__(self) -> None:
        self.worklist=[] #создаем словарь - пустой список
        with open("words.txt",'r') as f:
            self.workslist=f.read().splitlines()         #заполняем его из файла words          
        self.quest=self.workslist[random.randint(0,len(self.workslist))]#вопрос - выбор случайный
        self.answer = ""    #ответ игрока - пока пусто     
        self.baraban=[50,150,"0",750,"Б",100,"x2",200] #барабан
        self.set_answer() #заполнение
        self.steps = len(self.quest)+3 #шаги игры - ходы пользователя - количество букв в слове +3
        self.score=0 #счет
        self.baraban_result=""
        self.win=""  #победа или поражение

    def set_answer(self): #первоначальное задание ответа
        for i in self.quest: #
            self.answer+="*" #ответ заполняем значками *


    def check_answer(self, letter): #проверка ответа
        self.steps=self.steps-1 #количество шагов уменьшается на 1 
        find_sym=self.answer.find("*") #поиск звездочки в слове
        if find_sym==-1: #если звездочка не найдена
            self.win="gamer"
        if self.steps<=0: #если количество шагов меньше 0
            self.win="comp" 
        find = self.quest.find(letter) #ищем букву в задании quest
        if find==-1: #если не найдена 
            return 0 #возвращается 0 такой буквы нет
            #изменений в answer не происходит
        else:
            #очищается и снова заполняется answer
            # в принципе можно воспользоваться строковыми функциями
            # но мы переберем все варианты этой буквы
            # и соберем заново слово-ответ 

            list_answer = list(self.answer) # делим слово answer на список букв
            self.answer ="" #и очищаем его
            count=0
            for i in self.quest:
                if i==letter: #если буква на этом месте
                    self.answer+=letter
                else:
                    self.answer+=list_answer[count]  

                count=count+1     


            #print(self.answer)
   
            return 1 #возвращается 1 - такая буква есть

    def check_word(self,word): #проверка слова
        if word==self.quest: #если слово равно слову-загадке
            self.win="gamer" # победил игрок
        else:                # иначе
            self.win="comp"  # победил комп


    def check_baraban(self): #проверка показаний барабана
        if self.baraban_result=="Б": #если выпал Банкрот
            self.score=0
        elif self.baraban_result=="0": #переход хода
            self.steps=self.steps-1 #количество шагов уменьшается на 1
        elif self.baraban_result=="x2": #
             self.score=self.score*2


            
