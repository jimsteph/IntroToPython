# Exercise 8.5

while True:
    fname = raw_input("Enter a file name: ")
    try:
        fhand = open(fname)
        break
    except:
        print "Not a valid file name."

count = 0
for line in fhand:
    if line.startswith("From "):  # this will ignore any lines that start with "From:"
        words = line.split()
        if len(words) >=2:
            count = count + 1
            print words[1]
            
print "There were " + str(count) + " lines in the file with From as the first word"