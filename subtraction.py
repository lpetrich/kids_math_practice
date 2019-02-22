import random

a = random.randint(0, 20)
b = random.randint(0, 20)
while (b > a):
	a = random.randint(0, 20)
	b = random.randint(0, 20)
	continue

print "%3d" % a
print "-%2d" % b
c = input("----\n")
if int(c) == (a - b):
	print "Correct!"
else:
	print "The correct answer is ", a-b