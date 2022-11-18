#                                   vorkommen
# Nimmt die Anzahl des des Buchstabens und schreibt ihn dahinter ins Dictionary
#-------------------------------------------------------------------------------
def vorkommen(text):
    dictionary = {}
    anzahl = 1
    buchstabe = ""
    for i in text:
        buchstabe += i
        if buchstabe == i:
            anzahl + 1
        else:
            dictionary.update({buchstabe:anzahl})
    return dictionary

text = input("Text : ")
print(vorkommen(text))