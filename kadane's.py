def sum_subarr(arr):
    curr_sum =  max_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(curr_sum, max_sum)
    return max_sum

arr = [0,2,-3,4,2]
print(sum_subarr(arr))
