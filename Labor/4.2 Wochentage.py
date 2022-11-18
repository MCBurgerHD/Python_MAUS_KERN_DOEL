tage_dict = {
    0: "Fehler" , 1: "Montag", 2: "Dienstag", 3: "Mittwoch", 4: "Donnerstag", 5: "Freitag", 6: "Samstag", 7: "Sonnatg", }
def woche_function(tag_zahl):
    try:
        a = int(tag_zahl)
    except:
        a= 0
    if a not in range(1,8):
        a = 0
    return tage_dict[a]
 
b = input("Geben Sie eine Zahl zwischen inklusiv eins und 7 ein : ")
print(woche_function(b))