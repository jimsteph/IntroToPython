# Exercise 7.3
fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print "NA NA BOO BOO TO YOU - You have been punk'd!"
    else:
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