#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:21:28 2019

@author: rohit
"""

# program to count total number of Inversion in array in O(nlogn) complexity
# using divide and conquer technique

#arr = [2,6,8,1,9,3]  # here inversion is ((2,1),(6,1),(6,3),(8,1),(8,3),(9,3)) 
                     # total no = 6
                     
                     
def mergeANDcount(left, right, inverse=0):
    """
    return : sorted merge of left and right
             and total number of inverse
    """
    #print(left,right,inverse)
    result = []
    i,j = 0,0
    
    while i<len(left) and j<len(right):
        
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
            
        elif right[j]<left[i]:
            result.append(right[j])
            j += 1
            inverse += len(left[i:])
            
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
    
    return result, inverse
#
def countInversion(arr):

    if len(arr) == 1:
        return arr, 0
    
    
    mid = len(arr)//2
    
    left, leftcount = countInversion(arr[:mid])
    right, rightcount = countInversion(arr[mid:])

    return mergeANDcount(left,right,leftcount+rightcount)
#    
  
import time

arr = []
file = open("sample.txt","r")
start = time.time()
for word in file:
    arr.append(int(word.strip()))
file.close()

print(len(arr))
end = time.time()
print(end-start)
    
tic = time.time()
print(countInversion(arr)[1])
toc = time.time()

print(toc-tic)
