def bubble_sort(arr, show_steps=False):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if show_steps:
                print(arr)
    return arr, comparisons, swaps
