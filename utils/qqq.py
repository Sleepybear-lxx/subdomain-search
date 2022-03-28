import sys

for i in xrange(1000000):
	sys.stdout.write('\r'+str(i))

	sys.stdout.flush()