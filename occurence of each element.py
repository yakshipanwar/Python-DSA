def getdata():
    a= []
    arr = int(input())
    for i in range(arr):
        a.append(int(input()))
    return a

def check():
    a = getdata()
    b = set(a)
    cout = 0
    for i in b:
        for j in a:
            if i == j:
                cout+=1
        print(f"occurence of {i} in array: {cout}" )
        cout = 0
            
check()        
