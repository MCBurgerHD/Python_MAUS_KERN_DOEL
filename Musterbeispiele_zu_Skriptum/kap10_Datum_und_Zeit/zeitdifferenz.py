from datetime import date, timedelta, time, datetime

heute = date.today()
christmas = date(heute.year, 12, 24)
differenz = christmas - heute
print('Noch', differenz.days, 'Tage bis Weihnachten')
# Noch 343 Tage bis Weihnachten
print('Das sind', differenz.seconds, 'Stunden')
# Das sind 0 Stunden - date-Objekt - besitzt keine Zeitinformation
print('Weil:', differenz)                       # 343 days, 0:00:00

# nochmal mit datetime-Objekten
heute = datetime.now()                          # 2020-01-16 20:37:54.945143
print(heute)
christmas = datetime(heute.year, 12, 24) 
differenz = christmas - heute
print(differenz)                                # 342 days, 3:22:05.054857
print('Tage:', differenz.days)                  # Tage: 342
print('Zeit in gesamten Sekunden:', differenz.seconds)   
                                        # Zeit in gesamten Sekunden: 12125
stunden = differenz.seconds//3600
print('Stunden:', stunden)                      # Stunden: 3
print('Minuten:', differenz.seconds//60%60)     # Minuten: 22
print('Sekunden:', differenz.seconds%60)        # Sekunden: 5
print('Mikrosekunden:', differenz.microseconds) # Mikrosekunden: 54857
print('Das sind', 24 * differenz.days + stunden, 'Stunden')
                                                # Das sind 8211 Stunden
