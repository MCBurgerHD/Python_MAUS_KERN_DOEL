for z in 'abc':
	print(z)		# Gibt jedes Zeichen in eigener Zeile aus

s = ''
for i in range(65, 91):
    s += chr(i)
print(s)

for z in s:
    print(z.lower(), end = '')
