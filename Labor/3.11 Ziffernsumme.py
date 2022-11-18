for h in range(0,9):
    h+= 1
    for z in range(0,9):
        z+= 1
        for e in range(0,9):
            e+=1
            Ziffernsumme = h + z + e
            if(Ziffernsumme >25):
                print(h, z, e)