#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:21:28 2019

@author: rohit
"""

def merge(left, right):

    result = []
    i,j = 0,0
    
    while i<len(left) and j<len(right):
        
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
            
        elif right[j]<left[i]:
            result.append(right[j])
            j += 1
            
        else:
            result.append(left[i])
            i += 1
            result.append(right[j])
            j += 1
            
    while i<len(left):
        result.append(left[i])
        i += 1
    
    while j<len(right):
        result.append(right[j])
        j += 1
    
    return result

def mergesort(arr):
    global count
    
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)
    
import time

arr = []
file = open("sample.txt","r")
for word in file:
    arr.append(int(word.strip()))
file.close()

start = time.time()
arr = mergesort(arr)
end = time.time()

print("mergesort")
print(end-start, len(arr))
