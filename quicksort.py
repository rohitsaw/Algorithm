#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 20:48:50 2019

@author: rohit
"""

import random


def partition(arr,a, b):
    
    #print("before par")
    #print(arr)
    
    pivot = random.randint(a,b)
    #print(pivot)
    
    arr[pivot], arr[a] = arr[a], arr[pivot]
    
    i = a+1
    
    for j in range(a+1,b+1):
        if arr[j] < arr[a]:
            if j != i:
                arr[j] , arr[i] = arr[i], arr[j]
            i += 1
    arr[a], arr[i-1] = arr[i-1], arr[a]
            
    #print("after")
    #print(arr)
    return i-1

def quicksort(arr, start, end):
    
    if end > start:
    
        pv = partition(arr,start, end) # pv = right position of pivot element
    
        quicksort(arr, start, pv-1)
        quicksort(arr, pv+1, end)
    
    

import time    
l = [15,24,54,2,6,4,1,62]

arr = []
file = open("sample.txt","r")
for word in file:
    arr.append(int(word.strip()))
file.close()

start = time.time()
quicksort(arr,0,len(arr)-1)
end = time.time()

print("quicksort")
print(end-start, len(arr))
print("item at 5602 location " + str(arr[5602]))