import os.path
command = input()
if(command == "head"):

    filename = input("Name file(example: textforl):")
    filename = filename + ".txt"

    file_path = filename
    if(os.path.exists(file_path)):
        file = open(filename, 'r')
        lines = file.readlines()
        for i in range(10):
            print(lines[i])
    else:
        print("Файла нет")
else:
    print(command,"не является внутренней или внешней командой, исполняемой программой или пакетным файлом.")