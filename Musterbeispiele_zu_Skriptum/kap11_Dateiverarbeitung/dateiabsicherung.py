name = input('Bitte einen Dateinamen: ')
try:
    datei = open(name, 'r')
    print('Datei', name, 'konnte zum Lesen geöffnet werden')
    datei.close()
except:
    print('Datei', name, 'konnte zum Lesen nicht geöffnet werden')

