#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 19:44:40 2019

@author: rohit
"""


def dist(p,q):
    ''' return distance between two point'''
    import math
    x1, y1 = p[0], p[1]
    x2, y2 = q[0], q[1]
    
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def brute_force(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi
    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:  # Update min_dist and points
                    mi = d
                    p1, p2 = ax[i], ax[j]
    return p1, p2,mi
    

def closest_split_pair(px,py,d,mn):
    
    x_bar = px[len(px)//2][0]
    
    sy = []

    for point in py:
            if (x_bar-d <= point[0] <= x_bar+d):
                sy.append(point)
            
    best = d
    best_pair = mn
    
    l = len(sy)
    
    
    for i in range(l-1):
        for j in range(1,min(7,l-i)):
            p, q = sy[i], sy[i+j]
            dst = dist(p,q)

            if dst < best:
                best = dst
                best_pair = (p,q)

    return best_pair[0], best_pair[1], best
    
    


def closest_pair(px, py):
    
    if len(px) <= 3:
        return brute_force(px)
    
    mid = len(px)//2
    
    qx = px[:mid]
    rx = px[mid:]
    
    qy,ry = [],[]
    
#    midpoint = px[mid-1][0] # midpoint on x-axis
#    for x in py:
#        if x[0] <= midpoint:
#            qy.append(x)
#        else:
#            ry.append(x)
    
    temp = set(qx)
    
    for x in py:
        if x in temp:
            qy.append(x)
        else:
            ry.append(x)
            
    
    p1, q1, md1 = closest_pair(qx, qy)
    p2, q2, md2 = closest_pair(rx, ry)
    
    
    if md1 <= md2:
        d = md1
        mn = (p1,q1)
    else:
        d = md2
        mn = (p2,q2)
    
    p3, q3, md3 = closest_split_pair(px,py,d,mn)
    

    
    if d <= md3:
        return mn[0], mn[1], d
    else:
        return p3, q3, md3
    
point = [(2,1),(6,12),(3,11),(12,25),(16,13),(36,25),(45,2),(51,95),(77,8)]

px = sorted(point, key = lambda x:x[0])  #sorted by x-co-ordinates
py = sorted(point, key = lambda x:x[1])  # sorted by y-co-ordinate

print(closest_pair(px,py))
    
    
    
    

