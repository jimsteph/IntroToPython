tot = 0.0
cnt = 0
while True:
    val = raw_input('Enter a number: ')
    if val == 'done':
        break
    try:
        val = float(val)
        tot = tot + val
        cnt = cnt + 1
    except:
        print 'Invalid Data'
print tot, cnt, tot/cnt