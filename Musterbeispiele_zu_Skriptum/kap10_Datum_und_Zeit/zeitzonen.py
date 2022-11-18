import pytz
from datetime import datetime

utc = datetime.now(pytz.utc)
print(utc)                  # 2020-01-12 16:00:57.448340+00:00

localtime = utc.astimezone()
print(localtime)            # 2020-01-12 17:00:57.448340+01:00

wien = pytz.timezone('Europe/Berlin')
print(utc.astimezone(wien)) # 2020-01-12 17:00:57.448340+01:00
# neue Zeit - ein paar Milisekunden später
wientime = wien.localize(datetime.now())
print(wientime)             # 2020-01-12 17:09:05.656920+01:00

