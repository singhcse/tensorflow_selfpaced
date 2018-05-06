#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 20:37:31 2018

@author: shubhamcse
"""

class SimpleClass():
    def __init__(self,name):
        print("hello "+ name)
        
    def tell(self):
        print("tell me something")
        
        
        
        
x = SimpleClass
#class object
type(x)

y = SimpleClass('Shubham')
#instance
type(y)
y.tell()



class ExtendedClass(SimpleClass):
    def __init__(self):
        
        super().__init__('Shubham')
        print("Extended")
        
z=ExtendedClass()
z.tell()
        
        
        

        
        
        
        