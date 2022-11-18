import locale

lst = list("Textmitäa,öo,üundßbzw.ÄA,ÖO,ÜU")
print(lst)
# ['T', 'e', 'x', 't', 'm', 'i', 't', 'ä', 'a', ',', 'ö', 'o', ',', 'ü', 'u', 'n', 'd', 'ß', 'b', 'z', 'w', '.', 'Ä', 'A', ',', 'Ö', 'O', ',', 'Ü', 'U']
# normale Sortierung – ohne Berücksichtigung der Umlaute
listNeu = sorted(lst)
print(listNeu)
# [',', ',', ',', ',', '.', 'A', 'O', 'T', 'U', 'a', 'b', 'd', 'e', 'i', 'm', 'n', 'o', 't', 't', 'u', 'w', 'x', 'z', 'Ä', 'Ö', 'Ü', 'ß', 'ä', 'ö', 'ü'] 

# deutsche Sortierung – mit Berücksichtigung der Umlaute
locale.setlocale(locale.LC_ALL, 'german')   # Windows
# locale.setlocale(locale.LC_ALL, 'de_DE.utf8')   # Linux
listNeu = sorted(lst, key=locale.strxfrm)
print(listNeu)
# [',', ',', ',', ',', '.', 'a', 'A', 'ä', 'Ä', 'b', 'd', 'e', 'i', 'm', 'n', 'o', 'O', 'ö', 'Ö', 'ß', 't', 't', 'T', 'u', 'U', 'ü', 'Ü', 'w', 'x', 'z']
