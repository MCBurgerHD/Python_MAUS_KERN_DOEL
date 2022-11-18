plz = int(input("Postleitzahl : "))
bezirk = plz // 10 % 100

if bezirk <= 24 and bezirk >=1:
    print(bezirk , ". Bezirk")

else:
    print("Fehler")