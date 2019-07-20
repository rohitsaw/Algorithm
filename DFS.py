#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:11:23 2019

@author: rohit
"""



# topological sorting via dfa

def make_graph(file_name):
    '''
    read file and return dict representation of graph
    '''
    file = open(file_name, 'r')
    d = {}
    for line in file:
        line =list(map(str, line.split()))
        v = line.pop(0)
        d[v] = line
    return d

def DFS_TS(G):
    vertices = list(G.keys())
    temp = [False]*len(vertices)
    
    explore = dict(zip(vertices, temp))
    
    for v in vertices:
        if not explore[v]:
            DFS(G,v,explore)
    

def DFS(G,s,explore):
    global to
    global current_label
    
    explore[s] = True
    for v in G[s]:
        if not explore[v]:
            DFS(G,v,explore)
            
    to.append((s, current_label))
    current_label -= 1
    
    
#explore = set()     # keep track of explore vertex
to = []             # topological order

d = make_graph('dfs.txt')
current_label = len(d.keys())

DFS_TS(d)

print("topological order is")
to.sort(key=lambda x: x[1])

print(to)