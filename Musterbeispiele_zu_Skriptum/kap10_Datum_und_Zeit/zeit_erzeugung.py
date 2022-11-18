from datetime import datetime

now = datetime.now()
print(now)          # 2020-01-11 18:47:47.396608
# Timestamp in   yyyy-mm-dd hh:mm:ss.ms

print(now.year)     # 2020
print(now.day)      # 11
print(now.minute)   # 47

print(now.isoformat())                  # 2020-01-11T18:47:47.396608
print(now.strftime('%d.%m.%Y %H:%M'))   # 11.01.2020 18:47
