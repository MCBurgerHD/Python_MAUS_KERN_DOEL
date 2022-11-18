def printChars(zeichen, anzahl, zeilensprung):
    if zeilensprung:
        # print(zeichen*anzahl)
        print(str(zeichen)*anzahl)
    else:
        print(zeichen*anzahl, end = '')

printChars('x', 5, True)
printChars('o', 5, 0)
printChars(7, 4, 1)
printChars('3', 4, 1)
