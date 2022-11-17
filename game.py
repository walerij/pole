import random
class game:
    def __init__(self) -> None:
        self.worklist=[] #создаем словарь - пустой список
        with open("words.txt",'r') as f:
            self.workslist=f.read().splitlines()         #заполняем его из файла words          
        self.quest=self.workslist[random.randint(0,len(self.workslist))]#вопрос - выбор случайный
        self.answer = ""    #ответ игрока - пока пусто     
        self.baraban=[50,150,"0",750,"Б",100,"П",200] #барабан
        self.set_answer() #заполнение
        self.steps = len(self.quest)+3 #шаги игры - ходы пользователя - количество букв в слове +3
        self.score=0 #счет
        
        self.win=""  #победа или поражение

    def set_answer(self):
        for i in self.quest:
            self.answer+="*" 


    def check_answer(self, letter):
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


            print(self.answer)
            return 1 #возвращается 1 - такая буква есть
