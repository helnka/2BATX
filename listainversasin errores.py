#!/usr/bin/env python
# -*- coding: utf-8 -*-
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print "Dígame la palabra", (i+1)
        palabra = raw_input()
        lista+= [palabra]
    print("La lista creada es:", lista)

    inversas = []
for i in lista:
        inversa = inversa + [i]
print("La lista inversa es:", inversa)

