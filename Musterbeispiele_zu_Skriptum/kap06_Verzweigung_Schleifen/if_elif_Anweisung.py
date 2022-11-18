x = input('Text: ')

if not str.isalpha(x):
    print('{} besteht nicht nur aus Buchstaben'.format(x))
elif str.isupper(x):
    print('{} besteht  nur aus Großbuchstaben'.format(x))
else:
    print('{} beinhaltet auch Kleinbuchstaben'.format(x))
    
print('Jetzt geht es weiter')