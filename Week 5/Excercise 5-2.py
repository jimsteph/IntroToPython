maximum = None
minimum = None
while True:
    val = raw_input('Enter a number: ')
    if val == 'done':
        break
    try:
        val = int(val)
        tot = tot + val
        cnt = cnt + 1
        if maximum == None or val > maximum:
            maximum = val
        if minimum == None or val < minimum:
            minimum = val
    except:
        print 'Invalid input'
print "Maximum is", maximum
print "Minimum is", minimum
