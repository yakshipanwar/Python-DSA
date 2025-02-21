def getdata():
    a = []
    arr = int(input("enter the number of elements in array: "))
    for i in range(arr):
        a.append(int(input()))
    return a

def secondlarge():
    a = getdata()
    a.sort()
    return a[len(a) - 2]

print("second largest element: ",secondlarge())
