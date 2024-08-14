def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element from the array
    pivot = arr[len(arr) // 2]

    # Partition the array into three parts:
    # 1. Elements less than the pivot
    # 2. Elements equal to the pivot
    # 3. Elements greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively apply quick_sort to the left and right parts, and then concatenate the results
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
