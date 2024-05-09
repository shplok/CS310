# Problem Statement:
# You are given an amount of money in cents and a list of coin denominations.
# Write a function to find the minimum number of coins required tto make up that amount of money.
# Assume you have an infinite supply of each coin denomination.

# Sample input: Amount: 63 coin denominations [1,5,10,25]
# Sample output: 6 (Explanantion: 25 + 25 + 10 + 1 + 1 + 1 = 63)

# go with the heighest denomination until the number is reached.


def min_coins(amount, coins):
    coins.sort(reverse=True)
    # to get the demarkations in the order we need
    min_coin = 0


    for coin in coins:
        #loop through the coins
        count = amount // coin
        min_coin += count
        # increment the count by needed coins
        amount -= count * coin

        # until the amount is zero, keep decrementing by the count times the coin index value and then return min_coin

    if amount > 0: 
        return -1
    else:
        return min_coin


amount = 63
coins = [1,5,10,25]
print(min_coins(amount, coins))