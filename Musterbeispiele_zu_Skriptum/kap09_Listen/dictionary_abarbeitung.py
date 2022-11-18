dic = {'Rot' : 0xff0000, 'Grün' : 0x00ff00, 'Blau' : 0x0000ff, 'Weiß' : 0xffffff}
print(dic)  # {'Rot': 16711680, 'Grün': 65280, 'Blau': 255, 'Weiß': 16777215}

for k in dic:
    print('Die Farbe', k,'hat den Farbwert:', hex(dic[k]))
# Die Farbe Rot hat den Farbwert: 0xff0000
# Die Farbe Grün hat den Farbwert: 0xff00
# Die Farbe Blau hat den Farbwert: 0xff
# Die Farbe Weiß hat den Farbwert: 0xffffff

# Erzeugen von Listen und Sets
print(dic.items())  # steht für die Schlüssel-Werte-Paare
# dict_items([('Rot', 16711680), ('Grün', 65280), ('Blau', 255), ('Weiß', 16777215)])
liste = [color for (color, code) in dic.items() if code != 0]
print(liste)    # ['Rot', 'Grün', 'Blau', 'Weiß']
s = {color for (color, code) in dic.items() if color < 'Schwarz'}
print(s)        # {'Blau', 'Grün', 'Rot'}
