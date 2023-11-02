# Binary Search Algorithm
# This algorithm is used to search for a specific element in a sorted list.
# It works by repeatedly dividing the search interval in half.

def binary_search(arr, element):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index.

        if arr[mid] == element:  # If the middle element is the target element.
            return mid
        elif arr[mid] < element:  # If the middle element is less than the target element.
            left = mid + 1  # Update the left bound of the search interval.
        else:
            right = mid - 1  # If the middle element is greater than the target element, update the right bound.

    return -1  # Element not found in the list.


# Example of usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15]
element_to_find = 7
result = binary_search(my_list, element_to_find)

if result != -1:
    print(f"The element {element_to_find} is found at index {result}.")
else:
    print(f"The element {element_to_find} is not in the list.")
