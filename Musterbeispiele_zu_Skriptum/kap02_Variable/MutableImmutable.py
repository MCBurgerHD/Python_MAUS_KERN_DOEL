a = 1			# Zahlen sind immutable
b = a
a = 3
print(a, b)
x = "Hallo"		# Texte sind immutable
y = x
x = "Welt"
print(y, x)
l1 = [1, 2, 3]	# Listen sind mutable
l2 = l1
print(l1, l2)
l2[1] = 1000
print(l1, l2)
