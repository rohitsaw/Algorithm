def solve(i, make,c,store):
    if make<0:
        return 0
    elif make==0:
        return 1
    if i>=len(c):
        return 0
    if (i,make) not in store.keys():
        store[(i,make)] = solve(i, make-c[i],c,store)+solve(i+1,make,c,store)
    return store[(i,make)]


# Complete the getWays function below.
def getWays(n, c):
    i = 0
    store = {}
    ans = solve(i,n, c, store)
    #print(ans)
    return ans

n, m = map(int, input().split())
c = list(map(int, input().split()))
print(getWays(n,c))




