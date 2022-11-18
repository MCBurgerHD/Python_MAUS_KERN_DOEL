from random import randint
a = randint (100, 400)
b = randint (100, 400)

if a < b:
    print("{:3d} < {:3d}".format(a, b))
else:
    if a > b:
        print("{:3d} > {:3d}".format(a, b))
    else:
        print("{:3d} = {:3d}".format(a, b))