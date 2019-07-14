def partition(A, start, end):
    """ A : array
        start : start index
        end : end index exclusive
    """
    
    
    p = (end+start)//2
    
    A[start], A[p] = A[p], A[start]
    
    
    i = start+1
    for j in range(start+1, end):
        if A[j] < A[start]:
            if i != j:
              A[i], A[j] = A[j], A[i]  
            i += 1
    A[start], A[i-1] = A[i-1], A[start]

    return i-1
            

def Rselection(A, i, start, end):
    """ A : array
        i : required ith element
    """
    
    #print(A, i)
    
    #print(f"start = {start}, end = {end}")
    
    if end-start == 1:
        return A[start]
    
    
    if end - start > 1:
    
        j = partition(A,start,end)

    
        if j == i-1:
            return A[j]
        if j > i-1:
            return Rselection(A, i, start, j)
    
        if j < i-1:
            #i = i - (j + 1)
            return Rselection(A, i, j+1, end)


arr = []
file = open("sample1.txt","r")
for word in file:
    arr.append(int(word.strip()))
file.close()



t = 9025


import time

start = time.time()
print(Rselection(arr, t, 0, len(arr) ))
end = time.time()

print(end-start)



arr = []
file = open("sample.txt","r")
for word in file:
    arr.append(int(word.strip()))
file.close()

start = time.time()
arr.sort()
print(arr[t-1])
end = time.time()

print(end-start)


    