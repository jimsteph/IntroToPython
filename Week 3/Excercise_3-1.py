hours = float(raw_input("Enter Hours: "))
rate = float(raw_input("Enter Rate: "))
if hours >40.0 :
    regHours = 40.0
    overTime = hours - 40.0
else :
	regHours = hours
	overTime = 0
pay = (regHours * rate) + (overTime * rate * 1.5)
print round(pay, 2)