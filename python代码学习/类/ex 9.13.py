from random import randint

class Die:
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))

A = Die()
for i in range(1,11):
    A.roll_die()

B = Die(10)
for i in range(1,11):
    B.roll_die()
    
C = Die(20)
for i in range(1,11):
    C.roll_die()