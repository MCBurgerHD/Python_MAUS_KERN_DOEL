def f(a, b, c = 1, d = 0):
	print(a, b, c, d)

f(1, 2, 3, 4)			# Ausgabe von 1 2 3 4
f(1, 2, 3)			    # Ausgabe von 1 2 3 0
f(1, 2)				    # Ausgabe von 1 2 1 0
f(a = 1, b = 2, d = 3)	# Ausgabe von 1 2 1 3
f(d = 1, b = 2, a = 3)	# Ausgabe von 3 2 1 1
f(4, 3, d = 1)			# Ausgabe von 4 3 1 1
#  f(4)					# Fehler – Parameter b fehlt
#  f(b = 2, c = 3)		# Fehler – Parameter a fehlt
