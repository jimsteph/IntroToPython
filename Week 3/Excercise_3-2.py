rHours = raw_input("Enter Hours: ")
try:
    hours = float(rHours)
    rRate = raw_input("Enter Rate: ")
    try:
        rate = float(rRate)
        if hours >40.0 :
            regHours = 40.0
            overTime = hours - 40.0
        else :
            regHours = hours
            overTime = 0
        pay = (regHours * rate) + (overTime * rate * 1.5)
        print "Pay: " + str(round(pay, 2))
    except:
        print "Error, please enter numeric input"
except:
    print "Error, please enter numeric input"