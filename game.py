import random
class game:
    def __init__(self) -> None:
        self.worklist=[] #создаем словарь - пустой список
        with open("words.txt",'r') as f:
            self.workslist=f.read().splitlines()         #заполняем его из файла words          
        self.quest=self.workslist[random.randint(0,len(self.workslist))]#вопрос - выбор случайный
        self.answer = ""
        self.set_answer()
        #self.set_answer()
        self.win=""  

    def set_answer(self):
        for i in self.quest:
            self.answer+="*"          