def datum(datei):
    fobj = open(datei, "r")
    l2012 = []
    l2013 = []
    l2014 = []
    l2015 = []
    l2016 = []
    l2017 = []
    l2018 = []
    l2019 = []
    for i in fobj:
        if i == 2012:
            l2012 += i
        if i == 2013:
            l2013 += i
        if i == 2014:
            l2014 += i
        if i == 2015:
            l2015 += i
        if i == 2016:
            l2016 += i
        if i == 2017:
            l2017 += i
        if i == 2018:
            l2018 += i
        if i == 2019:
            l2019 += i
    fobj.write(l2012, l2013, l2014, l2015, l2016, l2017, l2018, l2019)
    fobj.close()
    
    

datum("jahresinfos.csv")