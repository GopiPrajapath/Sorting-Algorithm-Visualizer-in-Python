def quick_sort(arr, show_steps=False):
    comparisons = [0]
    swaps = [0]

    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps[0] += 1
            if show_steps:
                print(arr)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps[0] += 1
        if show_steps:
            print(arr)
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return arr, comparisons[0], swaps[0]
