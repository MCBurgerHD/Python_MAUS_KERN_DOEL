from random import randrange
note = randrange(0, 99)

if note < 59:
    if note == 0 or note == 1:
        print("F-")
    elif note == 58 or note == 59:
        print("F+")
    else:
        print("F")
elif note < 69:
    if note == 60 or note == 61:
        print("D-")
    elif note == 68 or note == 69:
        print("D+")
    else:
        print("D")
elif note < 79:
    if note == 70 or note == 71:
        print("C-")
    elif note == 78 or note == 79:
        print("C+")
    else:
        print("C")
elif note < 89:
    if note == 80 or note == 81:
        print("B-")
    elif note == 88 or note == 89:
        print("B+")
    else:
        print("B")
else:
    if note == 90 or note == 91:
        print("A-")
    elif note == 98 or note == 99:
        print("A+")
    else:
        print("A")