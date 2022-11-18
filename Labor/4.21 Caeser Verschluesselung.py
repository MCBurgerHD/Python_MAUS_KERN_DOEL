#                           caeser
#Verschlüsselt den eingegebenen Text in der Caeser Verschluesselung
def caeser(text, rotation):
    geheimtext = ''
    for i in text:
        zahl = ord(i)
        neuzahl = zahl + rotation
        if neuzahl > ord('Z'):
            neuzahl = neuzahl - 26
        neuesZeichen = chr(neuzahl)
        geheimtext = geheimtext + neuesZeichen
    return geheimtext
    
text = input("Text : ")
rotation = int(input("Rotation der Verschluesselung : "))

verschluesselt = caeser(text, rotation)
print(verschluesselt)