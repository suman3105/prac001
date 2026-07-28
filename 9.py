from collections import Counter

# Number of shoes
X = int(input())

# Shoe sizes in the shop
shoes = list(map(int, input().split()))

# Count how many shoes of each size are available
stock = Counter(shoes)

# Number of customers
N = int(input())

money = 0

for _ in range(N):
    size, price = map(int, input().split())

    if stock[size] > 0:
        money += price
        stock[size] -= 1

print(money)
