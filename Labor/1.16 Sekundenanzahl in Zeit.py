sek = int(input("Sekundenanzahl : "))

h = sek // 3600
minuten = sek // 60 % 60
sek1 = sek % 60

print("{:02d}".format(h) , ":" , "{:02d}".format(minuten) , ":" , "{:02d}".format(sek1))