import os
x=os.listdir('c:\windows\system32')

for i in list(x):
	if i[-3:]=='exe':
		print i