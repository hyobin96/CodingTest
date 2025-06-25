arr = [3, 1, 5, 2, 4]

def quick_sort(arr, low, high):
    if low < high:
        mid = partition(arr, low, high)

        quick_sort(arr, low, mid - 1)
        quick_sort(arr, mid + 1, high)


def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]


    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

quick_sort(arr, 0, 4)
print(*arr)