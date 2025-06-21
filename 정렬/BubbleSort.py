arr = [4, 3, 2, 1, 5]
n = len(arr)

for i in range(1, n):
    is_sorted = True
    for j in range(n - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            is_sorted = False

    if is_sorted:
        break

print(*arr)
