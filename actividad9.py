#!/usr/bin/env python
# -*- coding: utf-8 -*-
def rectangle (x,y,z):
	for i in range(x):
		for j in range(y):
			print z,
		print 			
print "Dime la amplaria del rectangle"
amplaria = input()
print "Dime la altura "
altura= input ()
print "Dime el caracter"
caracter = raw_input()
rectangle(altura,amplaria,caracter)
