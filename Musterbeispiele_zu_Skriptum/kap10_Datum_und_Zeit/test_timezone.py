import datetime
import pytz

# datetime object with timezone awareness:
print(datetime.datetime.now(tz=pytz.utc))

# seconds from epoch:
print(datetime.datetime.now(tz=pytz.utc).timestamp() )

# ms from epoch:
print(int(datetime.datetime.now(tz=pytz.utc).timestamp() * 1000) )

