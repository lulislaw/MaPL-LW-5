filename = "gadsbyIpart.txt"
file = open(filename, 'r')
lines = file.read().splitlines()
text = ""
specarr = ['.',',','-','!','?','"',':']
allwords = 0
count = 0
for i in range(len(lines)):
    text = text +" "+ lines[i]
for i in range(len(specarr)):
    text = text.replace(specarr[i],'')
words = text.split(" ")
allwords = len(words) - 1
print("Всего слов:",allwords)

for i in range(65,91):
    for w in range(1, len(words)):
        for c in range(len(words[w])):
            if i == ord(words[w][c]) or i+32 == ord(words[w][c]):
                count = count + 1
    print(chr(i) + chr(i+32),"\t",count,"\t",format(count/allwords, '0.2f') + "%")
    count = 0