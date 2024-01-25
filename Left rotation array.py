""" You have to rotate the array to the left based on the rotation count given
"""


def rotation_array(arr, d):
    n = len(arr)
    d = d % n  # ensures whether the count is a valid one
    rotated_array = arr[d:] + arr[:d]
    del arr
    return rotated_array


ar = [1, 2, 3, 4, 5]
count = 4
res = rotation_array(ar, count)
print(res)