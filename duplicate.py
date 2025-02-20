def getdata():
    a = []
    arr1 = int(input("enter the nuber of elements: "))
    for i in range(arr1):
        a.append(int(input()))    
    return a


def remov():
    el1 = getdata()
    return set(el1)


print(remov())


        
