print("1900 - 2012")
a = int(input("Начало "))
b = int(input("Конец "))
b = b + 1
def countnames(strr):
        arrnames = []
        arrcount = []
        for i in range(a, b):
            filename = "BabyNames/" + str(i) + strr
            file = open(filename, 'r')
            lines = file.read().splitlines()
            for i in range(len(lines)):
                arr = lines[i].split(" ")
                if not(arr[0] in arrnames):
                    arrnames.append(arr[0])
                    arrcount.append(0)
        for i in range(a, b):
            filename = "BabyNames/" + str(i) + strr
            file = open(filename, 'r')
            lines = file.read().splitlines()
            for i in range(len(lines)):
                arr = lines[i].split(" ")
                for l in range(len(arrnames)):
                    if arr[0] == arrnames[l]:
                        c = int(arr[1])
                        arrcount[l] = arrcount[l] + c
        x = zip(arrnames, arrcount)
        x = sorted(x, key=lambda tup: tup[1], reverse=True)
        print("Лучшие в сумме")
        for i in range(len(x)):
            print(x[i])

if(a >= 1900 and a < 2013 and b >= 1901 and b <= 2013):
    print("Муж.")
    countnames("_BoysNames.txt")
    print("Жен.")
    countnames("_GirlsNames.txt")
else:
    print("Указан неверный год")