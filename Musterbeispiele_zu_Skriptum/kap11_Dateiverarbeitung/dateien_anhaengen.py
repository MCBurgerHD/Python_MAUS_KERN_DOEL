from random import randint

datei = open("anhaengeDatei.txt", "a")
lst = [str(randint(1, 9)) for _ in range(5)]
datei.writelines(lst)       # Erzeugt 5 stellige Zahl - keine Leerzeichen
datei.write('\n')
datei.close()

datei = open("anhaengeDatei.txt", "a")
lst = [str(randint(1, 9))+' ' for _ in range(5)]
datei.writelines(lst)       # Erzeugt 5 einzelne Zahlen in einer Zeile
datei.write('\n')
datei.close()

datei = open("anhaengeDatei.txt", "a")
lst = [str(randint(1, 9))+'\n' for _ in range(5)]
datei.writelines(lst)       # Erzeugt 5 einzelne Zahlenzeilen
datei.close()
