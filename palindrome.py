def getdata():
    str1 = input("enter the string: ")
    return str1

def match():
    str1 = getdata()
    if str1 == str1[::-1]:
        print("string is palidrome")
    else:
        print("not palidrome")
        

match()
