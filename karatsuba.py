#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:49:40 2019

@author: rohit
"""

def split(temp, pos):
    temp = str(temp)
    
    return int(temp[:-pos]), int(temp[-pos:])

def multiply(x,y):
    assert type(x) == int
    assert type(y) == int
    
    
    #print(f"recursive call {x}, {y}")
#    if x<10 or y<10:
#        return x * y
#    
#    x = str(x)
#    y = str(y)
    
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y

    else:
        n = min(len(str(x)), len(str(y)))
        mid = n // 2
    
# =============================================================================
#         a = x // (10**mid)
#         b = x % (10**mid)
# 
#         c = y // (10**mid)
#         d = y % (10**mid)
# =============================================================================


        a,b = split(str(x), mid)
        c,d = split(str(y), mid)
    
        ac = multiply(a,c)
        bd = multiply(b,d)

    
        temp = multiply( a+b,c+d )   
        
        return ac*(10**(2*mid)) + (temp-ac-bd)*(10**mid) + bd


a = int(input("enter first number "))
b = int(input("enter second number "))

d = str(multiply(a,b)) 

print("By karatsuba method "+ d)

c = str( a*b )
print("By normal method " + c)

print(c == d)
    