from datetime import datetime, date, time

zeitpunkt = datetime(2020, 1, 13, 12, 10, 0)
print(zeitpunkt.isoformat())        # 2020-01-13T12:10:00
zeitpunkt = datetime(2020, 2, 29, 12, 10, 0)
print(zeitpunkt.isoformat())        # 2020-02-29T12:10:00
try:
    zeitpunkt = datetime(2019, 2, 29, 12, 10, 0)
except ValueError:
    print('Kein Schaltjahr!')
# nur Datum
belDatum = date(2020, 12, 12)
print(belDatum.isoformat())        # 2020-12-12
#nur Zeit
belZeit = time(23, 59, 12)
print(belZeit.isoformat())         # 23:59:12
