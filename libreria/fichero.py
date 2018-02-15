import os
import sys

def version():
     return 1.0

def crea_dir(directorio):
	if os.access(directorio,0):
		print "El directorio ya existe"
	else:
		os.mkdir(directorio)
		print "Directorio "+directorio+" creado"

def entorno():
	for clave,valor in os.environ.iteritems():
		if clave=='USER' or clave=='PATH' or clave=='SHELL':
			print valor


def gordos(directorio,size):
	if size[-1:].upper() not in ('K','M','G'):
		print "Solo K,M,G"
        tam=int(size[0:-1])
	if size[-1:].upper()=='K':
		bytes=tam*1024
	elif size[-1:].upper()=='M':
		bytes=tam*1024*1024
	else:
		bytes=tam*1024*1024*1024
	
	lista=os.listdir(directorio)
	for fichero in lista:
		if os.path.getsize(directorio+"/"+fichero)> bytes:
			print fichero+" "+ str(os.path.getsize(directorio+"/"+fichero))

def gordo2(path,size,formato):
	for x in os.listdir(path):
		if os.path.isfile(x):
			aux = int(os.path.getsize(x))
			print aux
			if size > aux:
				if formato == 'k':
					aux=aux*1024
					return aux
				elif formato == 'm':
					aux = aux*1024*1024
					return aux
				else:
					aux = aux*1024*1024*1024
					return aux
		 
def visualizar(fichero):
	f=open(fichero,'r')
	while True:
		linea=f.readline()
		if not linea:break
		print linea
