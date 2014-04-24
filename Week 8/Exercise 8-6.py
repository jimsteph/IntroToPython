# Exercise 8.6

numlist = []
while True:
    num = raw_input("Enter a number: ")
    try:
        num = float(num)
        numlist.append(num)
    except:
        if num == "done":
            break
        else:
            print "Not a number"

print "Maximum:", max(numlist)
print "Minimum:", min(numlist)