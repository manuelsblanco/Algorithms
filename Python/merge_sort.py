def merge_sort(arr):
    # Base case: if the list has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point and divide the array into left and right halves
    left_half = arr[:len(arr) // 2]
    right_half = arr[len(arr) // 2:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_array = []
    left_index = right_index = 0

    # Compare elements from both halves and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # If there are any remaining elements in the left half, add them
    sorted_array.extend(left[left_index:])

    # If there are any remaining elements in the right half, add them
    sorted_array.extend(right[right_index:])

    return sorted_array


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
