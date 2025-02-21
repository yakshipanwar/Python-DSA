def getdata():
    a = []
    arr = int(input())
    for i in range(arr):
        a.append(int(input()))
    return a

def getdata1():
    b = []
    arr1 = int(input())
    for i in range(arr1):
        b.append(int(input()))
    return b

def mergearray():
    a = getdata()
    b = getdata1()
    a.extend(b)
    a.sort()
    return a

print(mergearray())
