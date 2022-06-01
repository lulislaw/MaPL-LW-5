def yearname(asd):
    arrnames = []
    arrcount = []
    arrmax = []
    for i in range(1900, 2013):
        filename = "BabyNames/" + str(i) + asd
        file = open(filename, 'r')
        lines = file.read().splitlines()
        for i in range(len(lines)):
            arr = lines[i].split(" ")
            if not(arr[0] in arrnames):
                arrnames.append(arr[0])
                arrcount.append(0)
    for n in range(1900, 2013):
        filename = "BabyNames/" + str(n) + asd
        file = open(filename, 'r')
        lines = file.read().splitlines()
        for i in range(len(lines)):
            arr = lines[i].split(" ")
            for l in range(len(arrnames)):
                if arr[0] == arrnames[l]:
                    c = int(arr[1])
                    arrcount[l] = c
        x = zip(arrnames, arrcount)
        x = sorted(x, key=lambda tup: tup[1], reverse=True)
        if not(x[0][0] in arrmax):
            arrmax.append(x[0][0])
    print(arrmax)

yearname("_BoysNames.txt")
yearname("_GirlsNames.txt")