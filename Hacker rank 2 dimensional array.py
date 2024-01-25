#hacker rank 2d array usecase code
#!/bin/python3

import math
import os
import random
import re
import sys
import ctypes

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
import os


def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    result = []

    for query in queries:
        q, x, y = query

        if q == 1:
            idx = ((x ^ lastAnswer) % n)
            arr[idx].append(y)

        elif q == 2:
            idx = (x ^ lastAnswer) % n
            lastAnswer = arr[idx][y % len(arr[idx])]
            result.append(lastAnswer)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
