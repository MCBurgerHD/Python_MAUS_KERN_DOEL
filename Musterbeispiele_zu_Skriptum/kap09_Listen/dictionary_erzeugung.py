d = {0:1, 1:10, 2:100, 1:1000}  # 2-ter Key 1 ersetzt Wert
print(dict)                 # <class 'dict'>    
print(d)                    # {0: 1, 1: 1000, 2: 100} Unikatsschlüssel!

dic = {'Rot' : 0xff0000, 'Grün' : 0x00ff00, 'Blau' : 0x0000ff, 'Weiß' : 0xffffff}
print(dic)  # {'Rot': 16711680, 'Grün': 65280, 'Blau': 255, 'Weiß': 16777215}

# Zugriff über Schlüssel - Index
print(dic['Rot'])           # 16711680
print(hex(dic['Blau']))     # 0xff - hex() wandelt Zahl in Hexadezimaldarstellung
try:
    print(dic['Grau'])      # erzeugt Fehlerobjekt - Grau nicht vorhanden!
except KeyError:
    print('Kein Schlüssel') # Ausgabe
print('Grau' in dic)        # False
print('Grün' in dic)        # True

# Zugriff über get-Methode
print(dic.get('Weiß'))      # 16777215
print(dic.get('Grau'))      # nicht vorhanden! - liefert None
print(dic.get('Lila', -1))  # -1 - gesetzter Alternativwert
print(dic.get('Weiß', -1)) 
