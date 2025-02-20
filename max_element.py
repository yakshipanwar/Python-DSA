def elements():
    a = []
    arr = int(input("number of elements in the array: "))
    for i in range(0, arr):
        a.append(int(input()))
    return a

def max_element():
    max1 = max(elements())
    return max1


print("maximum element: ",max_element())

    
    
