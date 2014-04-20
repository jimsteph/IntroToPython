# Exercise 6.5
str = 'X-DSPAM-Confidence: 0.8475'
confidence = float(str[str.find(':')+2:])
print confidence