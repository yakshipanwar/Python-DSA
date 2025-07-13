arr = [2,3,4,5,2,3,4]
def single_number(arr):
    result = 0
    for i in arr:
        result ^= i
    return result

print(f"the single appearing number : {single_number(arr)}")