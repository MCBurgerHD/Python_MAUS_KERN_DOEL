from random import randint

zufall = randint(1, 20)

if zufall in (1, 2, 3, 5, 7, 9, 11, 13, 17, 19):
    print(zufall, "ist prim")
else:
    print(zufall, "ist nicht prim")
