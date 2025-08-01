def merge_sort(arr, show_steps=False):
    comparisons = [0]
    swaps = [0]

    def merge_sort_recursive(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr

        mid = len(sub_arr) // 2
        left = merge_sort_recursive(sub_arr[:mid])
        right = merge_sort_recursive(sub_arr[mid:])

        return merge(left, right)

    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
            swaps[0] += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        if show_steps:
            print(merged)
        return merged

    result = merge_sort_recursive(arr)
    return result, comparisons[0], swaps[0]
