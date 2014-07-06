#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 3, 2014

@author: anroco

In python how to unpack a tuple in several variables?

En python ¿como desempaquetar una tupla en varias variables?
'''

#create a tuple
tupla = 3, 6, 2
print (tupla)

#unpack a tuple in variables
num1, num2, num3 = tupla
print(num1 + num2 + num3)

#the number of variables must be equal to the number of items of the tuple
num1, num2, num3, num4 = tupla
