def partition(arr, si, ei):
    pivot_element = arr[si]

    count = 0
    for i in range(si + 1, ei + 1):
        if arr[i] <= arr[si]:
            count += 1

    pivot_idx = count + si

    # Swap pivot to its correct position
    arr[si], arr[pivot_idx] = arr[pivot_idx], arr[si]

    i = si
    j = ei

    while i < pivot_idx and j > pivot_idx:
        if arr[i] <= pivot_element:
            i += 1
        elif arr[j] > pivot_element:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return pivot_idx


def quick_sort(arr, si, ei):
    if si >= ei:
        return

    pivot_idx = partition(arr, si, ei)

    quick_sort(arr, si, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, ei)


# Driver code
arr = [5,9,1,80,99,-8,99999,-89,830,20,9,44,70,1,23]

print("Before sorting:")
print(arr)

quick_sort(arr, 0, len(arr) - 1)

print("After sorting:")
print(arr)