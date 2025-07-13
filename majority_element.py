def getdata():
    a = []
    arr = int(input("size of array:"))
    for i in range(arr):
        a.append(int(input(f"enter elemrnt {i + 1}: ")))
    return a

def maj_element():
    a= list(getdata())
    count = 0
    candidate = None

    for i in a:
        if count == 0:
            candidate = i
        if i == candidate:
            count += 1
        else:
            count -= 1

    if a.count(candidate) > len(a)//2:
        return candidate
    

print(maj_element())