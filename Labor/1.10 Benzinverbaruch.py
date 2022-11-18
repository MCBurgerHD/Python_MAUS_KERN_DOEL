km1 = float(input("Kilomterstand bei dem letzten Tankstop : " ))
km2 = float(input("Kilometerstand bei dem heutigen Tankstop : "))
L = float(input("Benzinverbrauch in L : "))
E = float(input("Benzinpreis pro L :"))
km = km1 + km2
print("Durchschnittlicher Benzinverbrauch : " , L / km)
print("Durchschnitliche Benzinkosten : " , E / km)