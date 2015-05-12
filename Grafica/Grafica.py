#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math

# [OK]
def fncCuadratica(n):
	valores= []

	for i in xrange(n):
		i+=1
		valores.append(i**2)
	print "Cuadrática", valores, "\n\n"
	return valores

# [OK]
def fncCubica(n):
	valores= []

	for i in xrange(n):
		i+= 1
		valores.append(i*i*i)

	print "Cúbica", valores, "\n\n"
	return valores

# [OK]
def fncLogaritmica(n):
	valores= []

	for i in xrange(n):
		valores.append(math.log10(i+1))

	print "Logarítmica", valores, "\n\n"
	return valores

# [OK]
def fncNlogN(n):
	valores= []
	for i in xrange(n):
		i+=1
		valores.append(i*(math.log10(i)))

	print "NlogN", valores, "\n\n"
	return valores

if __name__ == '__main__':
	n= 10
	x = range(n)

	# Títulos
	plt.xlabel("$n$")
	plt.ylabel("$T(n)$")
	plt.title("Grafica de funciones")

	plt.plot(x, fncLogaritmica(n), label= "$O(log(n))$", marker = 'o')
	plt.plot(x, xrange(n), 		   label= "$O(n)$")
	plt.plot(x, fncNlogN(n), 	   label= "$N log(n)$", marker = '^')
	plt.plot(x, fncCuadratica(n),  label= "$O(n^{2})$")
	plt.plot(x, fncCubica(n), 	   label= "$O(n^{3})$", marker = 'x')

	#plt.plot(x, fncPolinomial(n), 	   label= "$O(n^{m})$")
	#plt.plot(x, fncExponencial(n), label= "Exponencial $O(2^{n})$")
	#plt.plot(x, fncFactorial(n), label= "Factorial")

	# Ajusta el eje Y de la gráfica
	plt.ylim([0,100])
	plt.grid(True, lw = 2, ls = '--', c = '.75')
	plt.legend(loc= "upper left")
	#plt.savefig("grafica1.png", c= 'k')
	plt.show()


