#------------------------------------------------------------------------------------
#                                  ip_adresse
# Splitet die übergebene IP-Adresse, und überprüft diese ob sie aus Ganzhalen besteht
#------------------------------------------------------------------------------------
def ip_adresse(ip):
    splitip = ip.split(".")
    for i in splitip:
        try:
            i = int(i)
            nochmal = False
        except:
            return "ungültig"
        if nochmal == False and i < 100:
            return "gültig"
        else:
            return "ungültig"

ip = input("IP-Adresse : ")
print(ip_adresse(ip))