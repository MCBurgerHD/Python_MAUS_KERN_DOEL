#----------------------------------------------------------------
# Maximilian Ertl
# 27.5.2021
#                       fliter_lines
# Gibt nur die Zeilen der Datei aus, die den Suchstring enthalten
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#                   filter_lines
# Fuegt i in die Liste hinzu wenn dieser in pattern entahlten ist
#-----------------------------------------------------------------
def filter_lines (lines, pattern):
    lst = []
    for i in lines:
        if pattern in i:
            lst.append(i)
    return lst

file = open ("Dateiverarbeitung/Nationalratswahl2017.csv","r")
lines = [line.rstrip()for line in file.readlines()]
file.close ()
filtered = filter_lines(lines,"Pölten")
for line in filtered:
    print(line)