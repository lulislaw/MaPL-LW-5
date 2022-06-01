filename = "elements.txt"
file = open(filename, 'r')
lines = file.read().splitlines()
protonarr = []
shortname = []
longname = []
for i in range(len(lines)):
    x = lines[i].split(',')
    protonarr.append(x[0])
    shortname.append(x[1])
    longname.append(x[2])
command = input("Enter name or number: ")
while command != "":
    found = 0
    for i in range(len(protonarr)):
        if command == protonarr[i]:
            print(shortname[i],longname[i])
            found = 1
        if command == shortname[i]:
            print(protonarr[i], longname[i])
            found = 1
        if command == longname[i]:
            print(protonarr[i], shortname[i])
            found = 1
    if found == 0:
        print("Not found")
    command = input("Enter name or number: ")