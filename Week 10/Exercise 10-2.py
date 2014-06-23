# Exercise 10.2

fname = raw_input('Enter the file name: ')
try: 
    fhand = open(fname)
except:
    print 'File cannot be opened: ', fname
    exit()
    
for line in fhand:
    words = line.split()
    if (line.startswith('From') and not line.startswith('From:')):
        print line
        wds = split(line)
        print wds
