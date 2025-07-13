arr = [1,2,3,4]
n = 2
def compute_power(arr,n):
    return [x ** n for x in arr]


print(compute_power(arr,n))