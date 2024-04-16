import time


def selection_sort_visualized(arr):
    n = len(arr)
    # Iterate over all elements in the list
    for i in range(n):
        # Find the index of the smallest element in the remaining list
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the smallest element with the element at the current position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Print the current state of the list
        print("Step", i + 1, ":", arr)
        # Wait a short period to visualize each step (optional)
        time.sleep(0.5)


# Example of usage
arr = [64, 25, 12, 22, 11]
print("Original list:", arr)
print("Sorting process:")
selection_sort_visualized(arr.copy())  # Pass a copy to keep the original list unchanged
print("Sorted list:", arr)
