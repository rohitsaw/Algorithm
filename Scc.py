#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:36:50 2019

@author: rohit
"""

from collections import defaultdict


def make_graph(file_name):
    '''
    read file and return dict representation of graph
    '''
    file = open(file_name, 'r')
    d = {}
    for line in file:
        line =list(map(int, line.split()))
        v = line.pop(0)
        d[v] = line
    return d

def transpose(G):
    d = {}
    for i in G.keys():
        for j in G[i]:
            d[j] = d.get(j,[])
            d[j].append(i)
    return d
    
def first_pass(G):
    explore = set()
    finishing = []
    
    def dfs(v):
        explore.add(v)
        for u in G[v]:
            if u not in explore:
                dfs(u)
        finishing.append(v)
    
    for u in G.keys():
        if u not in explore:
            dfs(u)
    print("finishing time is")
    print(finishing)
    return finishing

def second_pass(G,f_time):
    explore = set()
    leader = defaultdict(list)
    for u in reversed(f_time):
        if u not in explore:
            explore.add(u)
            stack = [u]
            while stack:
                item = stack.pop()
                for v in G[item]:
                    if v not in explore:
                        explore.add(v)
                        stack.append(v)
                leader[u].append(item)
    return leader

def kosaraju(graph):
    return second_pass(graph, first_pass(transpose(graph)))
#        

d = make_graph('DFS_SCC.txt')

print("strongly connected component is")
print(list(kosaraju(d).values()))