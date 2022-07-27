from random import random


print('Начинай первым,бери конфеты!)')
a = int(input())
sweets = 2021-a
players = [1,2]
while sweets != 0:
    b = 0
    c = 0
    if sweets >= a and sweets >= c:
        if 0 < a <29:
            b = b + a
            import random   
            c = random.randint(1,28)
            sweets = sweets- b - c
            print("А я возьму",c,"конфет!")
            a = b

            def replace_first(players):
                return players[1:] + players[:1]
                
            print('Бери конфеты(от 1 до 28!)')
            a = int(input())
            print("Ого! Осталось",sweets,"конфет!")

            def replace_first(players):
                return players[1:] + players[:1]
        else:
            print('Играй честно!')
            a = int(input())
    else:
        print("Осталось только",sweets,"конфет!")
        a = int(input())
else:
    if  players[-1] == 2:

        print('Ты выиграл, ура!')
    else:
        print('Ты проиграл, увы!')
