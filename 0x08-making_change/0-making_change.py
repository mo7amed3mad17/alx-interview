#!/usr/bin/python3
"""
Making chane file
"""


def makeChange(coins, total):
    """ making change function
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed for a total of 0

    # Iterate over each coin and update dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
