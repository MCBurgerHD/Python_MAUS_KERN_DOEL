x = 3           # Ganzzahl
print(x, type(x))
b = 'abc'       # String
c = "abc"
print(b, type(b))
print(c, type(c))
x = 3.12        # Dezimalzahl
print(x, type(x))
x = 3-4j        # Komplexe Zahl 
print(x, type(x))
f = True        # Logischer (Wahrheits)Wert
print(f, type(f))
print(f+2)      # False = 0 True = nicht 0 oder 1 -> rechnen möglich
if 1: print("1 entspricht True")    # -> Zahlen können als log. Werte verwendet werden
print(isinstance(f, bool))
t = (1,2,3)
print(t, type(t))
print(isinstance(t, tuple))
print(isinstance([1,2,3], list))
n = None
print(n, type(n))
