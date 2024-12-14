#!/usr/bin/python3
"""
Making chane file
"""


def makeChange(coins, total):
    """ make changes func
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for a more greedy exploration
    coins.sort(reverse=True)

    # Use a queue for BFS
    from collections import deque
    queue = deque([(0, 0)])  # (current_sum, coin_count)
    visited = set([0])  # Keep track of visited sums to avoid reprocessing

    while queue:
        current_sum, coin_count = queue.popleft()

        # Explore each coin
        for coin in coins:
            next_sum = current_sum + coin

            # If we reach the total, return the count
            if next_sum == total:
                return coin_count + 1

            # If the sum exceeds the total, skip
            if next_sum > total:
                continue

            # If this sum hasn't been visited yet, add it to the queue
            if next_sum not in visited:
                visited.add(next_sum)
                queue.append((next_sum, coin_count + 1))

    # If we exit the loop, no solution was found
    return -1
