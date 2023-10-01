# Bubble Sort Algorithm in Python

# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
# compares adjacent elements and swaps them if they are in the wrong order.
# The algorithm gets its name because smaller elements "bubble" to the top of the list.

def bubble_sort(arr):
    # Length of the array
    n = len(arr)

    # Outer loop: number of elements in the array
    for i in range(n):
        # Initialize a variable to check if any swapping happened
        swapped = False

        # Inner loop: Compare each pair of adjacent items and swap them if needed
        # We subtract 'i' because the last 'i' elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the swapped flag to True
                swapped = True

        # If no two elements were swapped, the list is sorted
        if not swapped:
            break


# Test the bubble_sort function
test_arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", test_arr)

bubble_sort(test_arr)
print("Sorted array:", test_arr)
