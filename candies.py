import sys
import heapq

def minStepsToReachTarget(target, candies):
    heapq.heapify(candies)  # Convert the candies list into a min-heap

    steps = 0
    while candies[0] < target:
        least_sweet = heapq.heappop(candies)
        second_least_sweet = heapq.heappop(candies)
        new_candy = least_sweet + 2 * second_least_sweet
        heapq.heappush(candies, new_candy)
        steps += 1

    return steps

# Example usage:
target = int(input())
candies = list(map(int, input().split()))
outputVal = minStepsToReachTarget(target, candies)
print(outputVal)