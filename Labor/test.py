tag = 30
monat = 5
jahr = 2006




print(int(((tag + (2.6 * monat -0.2) + jahr%10 + ((jahr%10)/4) + ((jahr%100)/4) - 2 * jahr%100) % 6)))