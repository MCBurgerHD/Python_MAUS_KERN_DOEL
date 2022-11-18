import locale

locale.setlocale(locale.LC_ALL, 'german')		  # für Windows
# locale.setlocale(locale.LC_ALL, 'de_DE.utf8')     für Linux
# locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')    für Mac
print(locale.format_string('%.3f', 2.5))
print('{:n}'.format(12.33))

s = '2,5'       # lokale Schreibweise
x = locale.atof(s)
print(x*2)

s = '2.53'       # ergibt lustiges Ergebnis -> Ganzzahl
x = locale.atof(s)
print(x*2)
