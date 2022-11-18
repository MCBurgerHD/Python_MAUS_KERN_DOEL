#------------------------------------------------------------------------------------------
# Maximilian Ertl
# 02.06.2021
#                        laengster_eintrag
# Das Programm bstimmt den laengsten Eintrag in der Datei "Nationalratswahl2021.csv".
#-------------------------------------------------------------------------------------------

#----------------------------------------------------------
#                       laengster_eintrag
# bestimmt den laengsten Eintrag in der uebergebenen Liste
#----------------------------------------------------------

def laengster_eintrag(lst):
    l= 0
    for i in range(0, len(lst)):
        if len(lst[i]) > l:
            l = len(lst[i])
    return l

datei = open("Dateiverarbeitung/Nationalratswahl2017.csv")
dateitext = datei.readlines()
print(laengster_eintrag(dateitext))