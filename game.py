import random
class game:
    def __init__(self) -> None:
        self.worklist=[]
        with open("words.txt",'r') as f:
            self.workslist=f.read().splitlines()                   
        self.quest=self.workslist[random.randint(0,len(self.workslist))]
        self.win=""        