for i in (12, 34, 45):
	print(i, end = ' ')	
print()

list = ['a', 2, 12.34]
for counter, item in enumerate(list):
	print(counter, item)

list = [1, 2, 3, 4, 5]
result = [x*x for x in list]		# bildet das Quadrat aller Listenelemente
print(result)						# [1, 4, 9, 16, 25]

result = [x*x for x in list if x%2 == 0]	# nur für gerade Zahlen
print(result)				# [4, 16]

result = [[x, x*x] for x in list]	# erzeugt Paare von Werten
print(result)		# [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]

dict = {x:x*x for x in list}
print(dict)		
