#!/usr/bin/env python3
import time, locale
name = input('Geben Sie Ihren Namen an: ')
print('Hallo %s!' % name)
# Datum und Zeit ohne aktueller Lokalisierung
zeit = time.strftime('Heute ist %A der %d. %B.')
print(zeit)
""" Datum und Zeit in aktueller Lokalisierung
    (Hinweis: die Lokalisierung funktioniert nicht, 
    wenn Sie das Script in Thonny ausführen)  """
locale.setlocale(locale.LC_ALL, '')
zeit = time.strftime('Heute ist %A der %d. %B.')
print(zeit)
