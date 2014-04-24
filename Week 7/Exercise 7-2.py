# Exercise 7.2
fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

count = 0
dspam = 0.0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence'):
        count = count + 1
        spampos = line.find(':')
        dspam = dspam + float(line[spampos + 1:])
print "Average spam confidence:", dspam/count