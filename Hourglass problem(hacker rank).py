""""For knowing more about the hourglass problem visit hacker rank and do try out data structures and algoritham
 module"""
def sum_hourglass(arr):
    max_sum = -float('inf')
    for i in range(4):
        for j in range(4):
            top = arr[i][j]+arr[i][j+1]+arr[i][j+2]
            mid = arr[i+1][j+1]
            bottom = arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            arr_sum = top + mid + bottom

            max_sum = max(max_sum,arr_sum)
            return max
