
from collections import deque
import heapq

def calculateMaxSubArray(arr, m):
    if m <= 0 or m > len(arr):
        print("Invalid subarray size")
        return []

    result = []
    dq = deque()  # stores indices

    for i in range(len(arr)):
        dq.append(arr[i])
        while len(dq) >= m:
            result.append(max(dq))
            dq.popleft()

    print(result)


# Example usage
calculateMaxSubArray([6, 5, 3, 2, 4, 5], 3)