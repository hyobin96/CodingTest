# Basic
left = 0
right = n - 1
last = -1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(mid)
        break

    if arr[mid] > target:
        right = mid - 1

    else:
        left = mid + 1



# LowerBound


while left <= right:
    mid = (left + right) // 2
    if arr[mid] >= target:
        last = mid
        right = mid - 1

    else:
        left = mid + 1

print(last)


# UpperBound

while left <= right:
    mid = (left + right) // 2
    if arr[mid] > target:
        last = mid
        right = mid - 1

    else:
        left = mid + 1

print(last)