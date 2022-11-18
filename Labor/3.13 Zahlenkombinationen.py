for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
                    n = 0
                    for i in [a, b, c, d]:
                        if i == 0:
                            n += 1
                        if n == 2:
                            print(a, b, c, d)