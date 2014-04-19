def computepay(h, r):
    if h > 40.0 :
        rh = 40.0
        ot = h - 40.0
    else :
        rh = h
        ot = 0
    return (rh * r) + (ot * r * 1.5)


rHours = raw_input("Enter Hours: ")
try:
    hours = float(rHours)
    rRate = raw_input("Enter Rate: ")
    try:
        rate = float(rRate)
        print "Pay: " + str(round(computepay(hours, rate), 2))
    except:
        print "Error, please enter numeric input"
except:
    print "Error, please enter numeric input"