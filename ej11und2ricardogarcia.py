#!/usr/bin/env python
# -*- coding: utf-8
def lista():
    print "Cuantos nombres tiene la lista"
    valores=int(input())
    if valores < 1:
        print("¡Imposible!")
    else:
        lista=[]
        for i in range(0,valores):
            print "Introduzca nombres"
            palabra=raw_input()
            lista+=[palabra]
            print lista
lista()
