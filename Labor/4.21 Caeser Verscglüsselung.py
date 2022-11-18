#                           caeser
#Verschlüsselt den eingegebenen Text in der Caeser Verschluesselung
def caeser(text):
    geheimtext = ''
    for i in text:
        zahl = ord(i)
        neuzahl = zahl + 3
        if neuzahl > ord('Z'):
            neuzahl = neuzahl - 26
        neuesZeichen = chr(neuzahl)
        geheimtext = geheimtext + neuesZeichen
    return geheimtext
    
text = input("Text : ")

verschluesselt = caeser(text)
print(verschluesselt)