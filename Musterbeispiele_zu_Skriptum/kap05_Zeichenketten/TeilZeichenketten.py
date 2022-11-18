s = 'abcdefghijklmnopqrstuvwxyz'

# Slicing Syntax
# s[n]  das n-te Zeichen -> 0 basiert!
# s[start:ende]  ende - start viele Zeichen start inkl. ende exkl.

print(s[3])         # Zugriff auf das Index_3 -> sprich vierte Zeichen
print(s[3:6])       # Teil von Index a bis exkl Index b [a; b[ -> b-a Zeichen
print(s[:3])        # alles bis exkl Index b [0; b[ -> b Zeichen
print(s[3:])        # alles ab Index ab [a; Rest] -> alle bis auf die ersten a Zeichen
print(s[-4])        # Zugriff auf viertletzte Zeichen -> a von hinten
print(s[-4:])       # alles ab dem viertletzte Zeichen -> ab dem a von hinten
print(s[25])        # letztes Zeichen - letzte erlaubte Nummer
print(s[-1])        # ebenso letztes Zeichen 
# print(s[26])      # Indexüberschreitung - Fehler - Index out of range
print(s[-26])       # erstes Zeichen
# print(s[-27])     # Indexüberschreitung - Fehler

# mit Schrittweite (Stride)
# s[start:ende:schrittweite]  von start inkl. bis ende exkl. in schrittweite
print(s[ : :2])     # jedes zweite Zeichen
print(s[ :10:2])     # von den ersten 10 jedes zweite Zeichen
print(s[10: :2])     # vab dem 10. Zeichen jedes zweite Zeichen
print(s[ : :-1])     # in umgekehrter Reihenfolge
print(s[ : :-2])     # jedes zweite Zeichen in umgekehrter Reihenfolge

# Achtung
print(s[0:10])
print(s[0:10:-1])   # leeres Ergebnis
print(s[10:0:-1])   # verkehrt von Index_10 bis Index_1

# besser bei verkehrter Reihenfolge die Konstrukte hintereinander
# z.B. zuerst die Teilkette ermitteln und diese danach umdrehen
print(s[:10][::-1]) # die ersten 10 Zeichen verkehrt

# leichter Verständlich
s1 = s[:10]         # speichert die ersten 10 Zeichen auf s1
print(s1[::-1])     # gibt in umgedrehter Reihenfolge aus
