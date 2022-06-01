import os.path

def chars(word):

    arrB = ['A','E','I','O','U','Y']
    arr = ['a','e','i','o','u','y']
    arrn = [0,0,0,0,0,0]
    arrhabe = [0,0,0,0,0,0]
    for l in range(len(arr)):
        for i in range(len(word)):

            if arr[l] == word[i] or arrB[l] == word[i]:
                arrhabe[l] = 1
                if arrn[l] == 0:
                    arrn[l] = i

    if (arrn[5] > arrn[4] and arrn[4] > arrn[3] and arrn[3] > arrn[2] and arrn[2] > arrn[1] and arrn[1] > arrn[0] and sum(arrhabe) == 6):
        print(word)



filename = input("Name file(enter to finish):")
while filename != "":
    filename = filename + ".txt"
    file_path = filename
    if (os.path.exists(file_path)):
        file = open(filename, 'r')
        lines = file.read().splitlines()
        for i in range(len(lines)):
            chars(lines[i])
    else:
        print("Файла нет")
    filename = input("Name file(enter to finish):")