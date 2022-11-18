def f1(x):
    print(x)
    x = 5		# Veränderung gilt nur für den Parameter 
    print(x)	# Ausgabe 5

x = 3
f1(x)			# Ausgabe zuerst 3 dann 5
print(x)		# Ausgabe 3, x ist unverändert
