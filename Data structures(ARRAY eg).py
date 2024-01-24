"""This is a simple searching technique in an array were we will be checking in an array if the sum of two
elements in that array is equal to the target variable and if yes then we will return those elements """
def array_sum_check(ar,t):
    for i in range(len(ar)-1):
        for j in range(len(ar)):
            if ar[i] + ar[j] == t:
                return ar[i],ar[j]

        j = i+1
        j = j+1

    i = 0
    i = i + 1

    return f"The target sum cannot be found in the array"


arr = [6, 5, 4, 3, 9, 8, 0]
target = 10
res = array_sum_check(arr, target)
print(res)