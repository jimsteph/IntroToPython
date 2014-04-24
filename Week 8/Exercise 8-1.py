# Exercise 8.1
def chop(t): # takes a list and removes the head and tail.  No return value.
    tlen = len(t)
    del t[tlen-1]
    del t[0]
    
def middle(t): # takes a list and returns all but the head and tail.
    tlen = len(t)
    u = t[1:tlen-1]
    return u
    

# Test the above two functions
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print "original list:", mylist
print "testing middle"
x = middle(mylist)
print "x:", x
print "mylist:", mylist
print "testing chop"
y = chop(mylist)
print "y:", y
print "mylist:", mylist
print mylist[15]