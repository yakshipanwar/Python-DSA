n = int(input())
arr = map(int, input().split())
for i in range(n):
    arr.append(int(input()))
    print(set(arr))
