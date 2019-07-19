#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 19:42:35 2019

@author: rohit
"""

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
           
        
def BFS(G,start,end):
    ''' G : graph dictionary
        s : 1st vertex from path is required
        t : 2nd vertex to path is required
    '''

    dist = {}  
    
    n = len(G.keys())
    
    try:
        G[start]
    except:
        return f": {start} not found"
    
    try:
        G[end]
    except:
        return f": {end} not found"
    
    import copy
    import queue
    q = queue.Queue(maxsize=n)
    q.put(start)
    explore = set()
    
    dist[start] = [start]
    while not q.empty():
        v = q.get()
        explore.add(v)
        for av in G[v]:
            if av not in explore:
                explore.add(av)
                q.put(av)
                dist[av] = copy.deepcopy(dist[v])
                dist[av].extend([av])
                
                
    return dist[end]

def main():
    file_name = input("enter graph text file name(eg: graph.txt) ")
    G = make_graph(file_name)
    
    start, end = map(str, input("enter start and end vertex ").split())
    
    return BFS(G,start, end)

if __name__ == "__main__":
    print(f"shortest path is {main()} ")
    
    
    

        
        
    
    
