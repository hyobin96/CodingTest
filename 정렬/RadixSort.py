arr = [325, 213, 423, 545, 12]
n = len(arr)

mod = 1
for _ in range(len(str(max(arr)))):
    radix_arr = [[] for _ in range(10)]
    
    for num in arr:
        radix_arr[(num // mod) % 10].append(num)

    mod *= 10

    store_arr = []

    for i in range(10):
        for j in range(len(radix_arr[i])):
            store_arr.append(radix_arr[i][j])

    arr = store_arr

print(*arr)

