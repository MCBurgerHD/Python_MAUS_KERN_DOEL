def f1(x):
	x = [4, 5]	# x erhält ein neues Objekt zugewiesen
	print(x)	# Ausgabe [4, 5]

x = [1, 3]
f1(x)			# Ausgabe [4, 5]
print(x)		# Ausgabe [1, 3]

print()

def f2(x):
	x.append(7)	# in x wird ein weiterer Wert – 7 - hinzugefügt
	print(x)	# Ausgabe des veränderten Objektes

x = [1, 3]
f2(x)			# Ausgabe [1, 3, 7]
print(x)		# Ausgabe [1, 3, 7]
