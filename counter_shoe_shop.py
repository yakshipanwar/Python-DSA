from collections import Counter

shoe = int(input())
shoe_size = list(map(int, input().split()))
shoe_count = Counter(shoe_size)

customer = int(input())
earning = 0

for _ in range(customer):
    size, prize = map(int, input().split())
    if shoe_count[size] > 0:
        earning += prize
        shoe_count[size] -= 1

print(earning)