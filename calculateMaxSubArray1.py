
from collections import deque
def calculateMaxSubArray(arr, m):
    if m < 0 or len(arr) < m:
        print("Invalid subarray size")
        return

    dq = deque()
    result = []

    for i in range(len(arr)):

        # # Remove indices that are out of the current window
        while dq and dq[0] <= i - m:
            dq.popleft()

        # Remove indices of smaller elements (they won't be needed)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)
        # Add result once the first window is formed
        if i >= m - 1:
            result.append(arr[dq[0]])


    return result


print(calculateMaxSubArray([6, 5, 3, 2, 4, 5], 3))


