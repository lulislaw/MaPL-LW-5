filename = "text4.txt"
file = open(filename, 'r')
count = 0
maxc = 0
lines = file.read().splitlines()
for n in range(len(lines)):
    for i in range(len(lines[n])):
        if lines[n][i] != " ":
            count = count + 1
        else:
            if maxc< count:
                maxc = count
            count = 0
print(maxc)
for n in range(len(lines)):
    for i in range(len(lines[n])):
        if lines[n][i] != " ":
            count = count + 1
        else:
            if count == maxc-1:
                print(lines[n][i-maxc+1:i])
            count = 0



