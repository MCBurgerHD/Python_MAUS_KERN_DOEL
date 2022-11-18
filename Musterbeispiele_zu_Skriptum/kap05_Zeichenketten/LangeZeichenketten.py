s = 'Text mit einfachem Hochkomma'
s = "Text mit doppelten Hochkomma"		# egal wie
print(s, type(s)) 		# Text mit doppelten Hochkomma <class 'str'> 

s = '''dies ist
ein langer
    Text, welcher
noch gelesen werden kann.
Allerdings ist die Darstellung
SCHRECKLICH!'''
print(s)
s = """dies ist \
ein langer \
Text, welcher \
noch gelesen werden kann. \
Allerdings ist die Darstellung \
SCHRECKLICH!"""
print(s)
s = "Die bessere Variante"
s += ", man setzt dies schön zusammen."      
s += "\nNun ist es leichter lesbar!"
print(s)

# Bildung durch Zusammenfügen und Vervielfachen
s1 = 'abc'
s2 = "efg"
print(s1 + s2)
print(s1 * 4)
print(s2 * 3)
print('x' * 30)

# Escapesequenzen
s = 'a\u0042c'      # Unicodesequenz
print(s)
print('abc\tdef')   # Tabulator
print('abc\rdef')   # Wagenrücklauf
print('abc\\def')   # als druckbare Zeichen
print('abc\'def')
print('abc\"def')
print('abc"def')    # Textmarkierung jetzt druckbar
print("abc'def")
# vorgestelltes r (raw) entwertet alle \  -> drucktechnisch dargestellt
print(r'Text\mit\vielen\Backslash\in\der\Zeile')

# Codenummern und umgekehrt
print(chr(65))  # Zeichen (Char) laut Codepagenummer
print(chr(97))
print(chr(8364))
print(ord('A'))  # Nummer (Ordinal) zum zugehörigen Zeichen
print(ord('a'))
print(ord('€'))
print(ord('1'))