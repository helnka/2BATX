#!/usr/bin/env python
# -*- coding: utf-8
d=0
m=0
r=0
s=0
letra=0
resultado=0
def suma(a,b):
    resultado=a+b
    return "El resultado es:",resultado
def resta(a,b):
    resultado=a-b
    return "El resultado es:",resultado
def multiplicacion(a,b):
    resultado=a*b
    return "El resultado es:",resultado
def division(a,b):
    resultado=a/b
    return "El resultado es:",resultado
print "S,R,M,D"
print "Introduzca un numero"
a=int(input())
print "Introduzca un numero"
b=int(input())
print "Introduzca una letra"
letra=raw_input()
while letra<>"si":
    if letra=="d":
        print division(a,b)
    if letra=="s":
        print suma(a,b)
    if letra=="m":
        print multiplicacion(a,b)
    if letra=="r":
        print resta(a,b)
    print "Introduzca una letra"
    letra=raw_input()
if letra=="si":
    print "MUY BIEN, HAS ACABADO!!!!"
