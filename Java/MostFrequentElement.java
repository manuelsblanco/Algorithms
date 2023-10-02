import java.util.HashMap;
import java.util.Map;

public class MostFrequentElementFinder {
  public static void main(String[] args) {
    int[] array = {1, 3, 1, 3, 2, 1};
    int mostFrequentElement = findMostFrequentElement(array);
    System.out.println("Most frequent element: " + mostFrequentElement);
  }

  // Function to find the most frequent element in an array
  static int findMostFrequentElement(int[] arr) {
    Map<Integer, Integer> frequencyMap = new HashMap<>();

    for (int element : arr) {
      // Update the frequency of the element in the map
      frequencyMap.put(element, frequencyMap.getOrDefault(element, 0) + 1);
    }

    int mostFrequentElement = -1;
    int maxFrequency = 0;

    for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
      int element = entry.getKey();
      int frequency = entry.getValue();

      if (frequency > maxFrequency) {
        maxFrequency = frequency;
        mostFrequentElement = element;
      }
    }

    return mostFrequentElement;
  }
}
