# Exercise 6.3
def count(word, letter):
    i = 0
    for l in word:
        if l == letter:
            i = i + 1
    print i

count('banana', 'a')			# should be 3
count('expedialidocious', 'e')	# should be 2
count('expedialidocious', 'x')	# should be 1
count('expedialidocious', 'i')	# should be 3
count('banana', 'n')			# should be 2
