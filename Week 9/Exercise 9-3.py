# Exercise 9.3

fname = raw_input('Enter the file name: ')
try: 
    fhand = open(fname)
except:
    print 'File cannot be opened: ', fname
    exit()
    
addresses = {}
for line in fhand:
    words = line.split()
    if (line.startswith('From') and not line.startswith('From:')):
        addresses[words[1]] = addresses.get(words[1],0) + 1
