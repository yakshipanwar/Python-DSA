number = int(input("enter the number: "))
power = int(input("enter the power: "))
n = int(input("enter the number: "))
r = int(input("enter the power: "))
def compute_power(number, power, n, r):
    p = pow(number, power)
    q = n ** r
    return p,q
print(compute_power(number,power,n,r))