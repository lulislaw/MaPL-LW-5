import os.path
command = input()
if(command == "cat"):
    newfilename =input("Имя для итогового файла: ")
    newfilename = newfilename + ".txt"
    my_file = open(newfilename, "w+")
    filename = input("Name file(example: textforl):")
    while filename != "":
        filename = filename + ".txt"
        file_path = filename
        if(os.path.exists(file_path)):
            file = open(filename, 'r')
            lines = file.readlines()
            for i in range(len(lines)):
                my_file.write(lines[i])
        else:
            print("Файла нет")
        filename = input("Name file(enter to finish):")


else:
    print(command,"не является внутренней или внешней командой, исполняемой программой или пакетным файлом.")
