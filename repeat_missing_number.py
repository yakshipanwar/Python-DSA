def getdata():
    a = []
    n = int(input("enter the size of array: "))
    for i in range(n):
        a.append(int(input(f"enter element {i + 1}: ")))
    return a


def find_repeat_and_missing(a):
    n = len(a)
    count = {}
    repeated = missing = None

    for i in a:
        count[i] = count.get(i, 0) + 1

    for i in range(1, n+1):
        if i not in count:
            missing = i
        elif count[i] == 2:
            repeated = i

    return repeated, missing


a = getdata()
repeat, miss = find_repeat_and_missing(a)
print(f"Repeated number: {repeat}")
print(f"Missed number: {miss}")