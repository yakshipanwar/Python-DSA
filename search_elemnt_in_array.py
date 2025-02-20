
def getdata():
    a = []
    arr = int(input("enter the array length: "))
    for i in range(arr):
        a.append(int(input()))
    return a

def search():
    element = getdata()
    x = int(input("enter the searched element: "))
    if x in element:
        print("number is present")
    else:
        print("not found")

search()


        
    
             
