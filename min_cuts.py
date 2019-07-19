import random
import copy
    

def RandomContraction(d):
    while len(d.keys()) > 2:
        rv1 = random.choice(list(d.keys()))
        rv2 = random.choice(list(d[rv1]))
        
        
        # mergeing two nodes
        d[rv1].extend(d[rv2])
        for x in d[rv2]:
            d[x].remove(rv2)
            d[x].append(rv1)
            
        # removing self loop
        while rv1 in d[rv1]:
            d[rv1].remove(rv1)
            
        del d[rv2]
        
    for key in d.keys():
        return len(d[key])
        

def main():
    
    d = {}
    m = 0
    file = open('graph.txt', 'r')
    for line in file:
        line = list(map(int, line.split()))
    
        v = line.pop(0)
        d[v] = line
        m += len(line)
        
    n = len( d.keys() )
    m = m//2

    temp = []
    
    k = 20  # no of iteration
            # k is large for large success probability
    for i in range(k):
        g = copy.deepcopy(d)
        temp.append( RandomContraction(g) )
        if not i%1000:
            print("----")
    
    return min(temp)


print( main() )