def getdata():
    a =[]
    arr1 = int(input("enter the number of elements: "))
    for i in range(arr1):
        a.append(int(input()))
    print(a)
    return a

def getdata1():
    b = []
    arr2 = int(input("enter the number of elements: "))
    for i in range(arr2):
        b.append(int(input()))
    print(b)
    return b

def intersec():
    c= []
    ele1 = getdata()
    ele2 = getdata1()
    for i in range(len(ele1)):
        for j in range(len(ele2)):
            if ele1[i] == ele2[j]:
                c.append(ele1[i])
    return c

print("intersection of two arrays: ",intersec())
                
                
