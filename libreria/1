import os
import sys

def gordo(path,size,formato):
	for x in os.listdir(path):
		if os.path.isfile(x):
			aux = os.path.getsize(x)
			if size > aux:
				if formato == 'k':
					return aux
				elif formato == 'm':
					aux = aux/1024
					return aux
				else:
					aux = aux/(1024*1024)
					return aux
		 
