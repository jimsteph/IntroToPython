# Exercise 8.4

rdict = list()
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for w in words:
        if w not in rdict:
            rdict.append(w)
rdict.sort()
print rdict