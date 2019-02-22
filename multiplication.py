import random

while True:
	print "###########################################################################\n"
	a = random.randint(0, 10)
	b = random.randint(0, 10)
	print "%4d" % a
	print "x%3d" % b
	ans = input("------\n")
	while int(ans) != a*b:
		print "Incorrect, please try again"
		print "%4d" % a
		print "x%3d" % b
		ans = input("------\n")
	print "Correct!!\n"
