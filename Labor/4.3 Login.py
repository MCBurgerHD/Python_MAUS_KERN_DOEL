def login(username, password):
    return username == "IF" and password == "If4yOu"

def change_password(old_password):
    alt = input("Password : ")
    if alt != old_password:
        print("Worng Password")
        print("-"*10)
        return old_password
    else:
        rueck = input("New Password : ")
        print("Your Password has been changed")
        print("-"*10)
    return rueck

user = "IF"
pw = "If4yOu"

nochmal = True
while nochmal:
    name = input("Username : ")
    wort = input("Password : ")
    print("-"*10)
    if login(name, wort):
        nochmal = False
    else:
        print("\nFehler Wiederholung\n")
print("Hello IF")
eingabe = "c"
while eingabe != "q":
    print("q ... quit")
    print("c ... change password")
    print("-"*10)
    eingabe = input("--> ")
    if eingabe == "c":
        pw = change_password(pw)
    elif eingabe != "q":
        print("Ungültige Auswahl")

print("Bye")