def getdata_1():
    a= []
    n = int(input("enter the size of array: "))
    for i in range(n):
        a.append(int(input(f"enter element {i + 1} of array 1: ")))
    return a

def getdata_2():
    b= []
    n = int(input("enter the size of array: "))
    for i in range(n):
        b.append(int(input(f"enter element {i + 1} of array 2: ")))
    return b

def merge_array():
    x = getdata_1()
    y = getdata_2()
    x.extend(y)
    x.sort()
    return x

print(merge_array())