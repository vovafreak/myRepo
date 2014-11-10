#/usr/bin/python

"""mylist = [x*x for x in range(5)]
for i in mylist :
	print(i)"""

def print_matches(matchtext):
	print "poisk podstroki", matchtext
	while True:
		line = (yield)
		if matchtext in line:
			print "matchtext is ", matchtext, "in line ", line

matchers = [print_matches("python"), print_matches("guido"), print_matches("jython")]
for m in matchers: 
	m.next()
wwwlog = open("/Users/miro69/test.txt", "rw+")
for line in wwwlog:
	for m in matchers:
		m.send(line)
		
wwwlog.close()

import fibo
fibo.fib(10)

