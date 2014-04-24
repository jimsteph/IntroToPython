# Exercise 8.2
# The last line of the program (print words[2]) is unguarded.  It will fail if it ever
# encounters a line that starts with "From" and only has one other word.  This could
# occur in the body of the email ("From me!").

# Here is the modified version that guards against it:

fhand = open('mbox-short-mod.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if len(words) >= 3: print words[2]
    