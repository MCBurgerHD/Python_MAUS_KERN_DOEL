print(str.isalpha('a'))
print("a".isalpha())
print(str.isalpha('abcABCÄÜÖäüö'))
print('öäß'.isalpha())
print(str.isalpha('abc123'))
print(str.isalpha(' '))
print(''.isalpha())
print(str.isdigit('a'))
print(str.isdigit('123'))
print(str.isalnum('abc123'))
print(str.isalnum('!'))
print(str.isascii('abc123|4!'))
print(str.islower('a'))
print(str.islower('abc123_'))
print('abs'.islower())
print(str.isupper('abcD'))
print(str.isnumeric('³'))
print(str.isnumeric('½'))
