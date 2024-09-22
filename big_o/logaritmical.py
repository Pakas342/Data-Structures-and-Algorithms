def binary_search(array, number_to_find):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == number_to_find:
            return mid
        elif array[mid] < number_to_find:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example usage:
arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, x)

if result != -1:
    print("Index of the element", str(result))
else:
    print("Element is not present in array")
