from datetime import *

# nur Datum
today = date.today()
print(today)            # 2020-01-12
now = datetime.now()
print(now.date())       # 2020-01-12
# nur Zeit
print(now.time())       # 15:58:30.3581437
# zusammenführen
datum = date.today()            
print(datum)                    # 2020-01-12
zeit = datetime.now().time()    
print(zeit)                     # 15:58:30.363436
zusammen = datetime.combine(datum, zeit)
print(zusammen)                 # 2020-01-12 15:58:30.363436
