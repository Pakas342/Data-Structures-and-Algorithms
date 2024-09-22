# O(n*log(n))
def quicksort(array_to_sort):
    if len(array_to_sort) <= 1:
        return array_to_sort

    pivot = array_to_sort[len(array_to_sort) // 2]
    left = [x for x in array_to_sort if x < pivot]
    middle = [x for x in array_to_sort if x == pivot]
    right = [x for x in array_to_sort if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# Example usage:
array = [3, 8, 2, 5, 1]
sorted_arr = quicksort(array)
print(sorted_arr)

