import os
import sys

x=raw_input('introduzca una letra')
y=os.listdir('c:\windows\system32')
c=0
for i in y:
	if i.count(x) > 0:
		#print i
		c=1+c
print "TOTAL letras "+str(x)+':'+str(c)	