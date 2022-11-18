from datetime import datetime
import locale

nun = datetime.now()
print(nun)                  # 2020-01-12 15:26:47.972153
# Ohne Lokalisierung
print(nun.strftime('%a, %d. %b %Y'))      # Sun, 12. Jan 2020
print(nun.strftime('%A, %d. %B %Y'))      # Sunday, 12. January 2020
# mit Lokalisierung - deutsch 
locale.setlocale(locale.LC_ALL, 'german') 
print(nun.strftime('%a, %d. %b %Y'))      # So, 12. Jan 2020
print(nun.strftime('%A, %d. %B %Y'))      # Sonntag, 12. Januar 2020

s = '2020-01-12 15:26'
dt = datetime.strptime(s, '%Y-%m-%d %H:%M')
print(dt)                                 # 2020-01-12 15:26:00
try:
    t = datetime.strptime(s, '%Y %m-%d %H:%M')  # falsche Format
except ValueError:
    print("Parsen nicht möglich")
