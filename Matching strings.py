def array_count(stringlist, arr):
    num = []
    for j in range(len(arr)):
        count = stringlist.count(arr[j])
        num.append(count)
    return num


slist = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']
res = array_count(slist, queries)
print(res)
