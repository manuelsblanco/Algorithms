public class QuickSort {

    // Method to implement Quick Sort
    public static void quickSort(int[] arr, int left, int right) {
        if (left < right) {
            // Partition the array and get the pivot index
            int pivotIndex = partition(arr, left, right);

            // Recursively apply Quick Sort to the subarrays
            quickSort(arr, left, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, right);
        }
    }

    // Method to partition the array
    private static int partition(int[] arr, int left, int right) {
        // Choose the rightmost element as the pivot
        int pivot = arr[right];
        int i = left - 1; // Index of the smaller element

        for (int j = left; j < right; j++) {
            // If current element is less than or equal to pivot
            if (arr[j] <= pivot) {
                i++;

                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Swap arr[i + 1] and arr[right] (or pivot)
        int temp = arr[i + 1];
        arr[i + 1] = arr[right];
        arr[right] = temp;

        return i + 1; // Return the partition index
    }

    // Utility method to print the array
    public static void printArray(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    // Main method to test Quick Sort
    public static void main(String[] args) {
        int[] arr = {38, 27, 43, 3, 9, 82, 10};
        System.out.println("Unsorted array:");
        printArray(arr);

        quickSort(arr, 0, arr.length - 1);

        System.out.println("Sorted array:");
        printArray(arr);
    }
}
