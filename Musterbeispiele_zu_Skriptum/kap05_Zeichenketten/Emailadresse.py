import re

pattern = r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]+$'
email = input("Geben Sie eine Email-Adresse ein: ")

if re.match(pattern, email):
    print("Die Email-Adresse ist OK")
else:
    print('Der Text entspricht nicht einer gültigen Email')
