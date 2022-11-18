for i in [7, 5, 9]:
	print(i, end=' ')	# Ausgabe 7 5 9
print()
print(i)		# Ausgabe 9	der zuletzt gespeicherte Wert!

for i in range(1, 10):
	print(i, end=' ')	# Ausgabe 1 2 3 4 5 6 7 8 9
print()

for i in range(0, 10, 3):	# in 3er Schritten
	print(i, end=' ')		# Ausgabe 0 3 6 9
print()

for i in range(100, 20, -10):	# in 10er Schritten runter
	print(i, end=' ')		# Ausgabe 100 90 80 70 60 50 40 30 
print()

for i in range(1, 9):
	x = i/10
	print(x, end=' ')	# Ausgabe 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
print()
