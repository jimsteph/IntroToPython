# Exercise 9.2

fname = raw_input('Enter the file name: ')
try: 
    fhand = open(fname)
except:
    print 'File cannot be opened: ', fname
    exit()
    
days = {}
for line in fhand:
    words = line.split()
    if (line.startswith('From') and not line.startswith('From:')):
        days[words[2]] = days.get(words[2],0) + 1

print days