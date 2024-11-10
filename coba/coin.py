coins = [2, 3, 5, 10, 15]

amount = int(input("masukan jumlah yang ingin dicapai: "))

count = 0

for coin in coins:
    while amount >= coin:
        amount -= coin
        count += 1

print("Jumlah coin yang diperlukan:", count)