from random import choice

A = ['1','2','3','4','5','6','7','8','9','10','a','b','c','d','e']

a = choice(A)
b = choice(A)
c = choice(A)
d = choice(A)
print(f"如果彩票上是{a}{b}{c}{d} 那你就中奖了")

my_ticket = ['1','2','3','4']
times = 0
while True:
    a = choice(A)
    b = choice(A)
    c = choice(A)
    d = choice(A)
    if [a,b,c,d] == my_ticket:
        print(f"{times}")
        break
    else:
        times+=1