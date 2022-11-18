from datetime import datetime, date, timedelta

heute = datetime.now().date()   # akt. Datum
week = timedelta(weeks = 1)     # Delta ist eine Woche
# heute  in 1 Woche  in 3 Wochen  vor 2 Wochen
print(heute, heute + week, heute + 3*week, heute - 2*week) 
# 2020-01-12 2020-01-19 2020-02-02 2019-12-29

heute = datetime.now()
minute = timedelta(minutes = 1)
bald = heute + 10 * minute
print(heute.time(), bald.time())
# 17:40:36.285250 17:50:36.285250
frueher = heute - 10 * minute
print(heute.time(), frueher.time())
# 17:40:36.285250 17:30:36.285250
hour = timedelta(hours = 1)
morgen = heute + 24*hour
print(morgen)
