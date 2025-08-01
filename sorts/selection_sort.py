def selection_sort(arr, show_steps=False):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            swaps += 1
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if show_steps:
            print(arr)
    return arr, comparisons, swaps
