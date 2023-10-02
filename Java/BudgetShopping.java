import java.util.Arrays;

public class BudgetShopping {
  // Solution 1: Using nested loops
  public static int getMoneySpent_v1(int[] keyboards, int[] drives, int b) {
    int maxTotal = -1;
    for (int keyboard : keyboards) {
      for (int drive : drives) {
        int total = keyboard + drive;
        if (total <= b && total > maxTotal) {
          maxTotal = total;
        }
      }
    }
    return maxTotal;
  }

  // Solution 2: Using Arrays.stream() and max()
  public static int getMoneySpent_v2(int[] keyboards, int[] drives, int b) {
    return Arrays.stream(keyboards)
      .flatMap(k -> Arrays.stream(drives).filter(d -> k + d <= b))
      .max()
      .orElse(-1);
  }

  public static void main(String[] args) {
    int[] keyboards1 = {3, 1};
    int[] drives1 = {5, 2, 8};
    int budget1 = 10;
    System.out.println(getMoneySpent_v1(keyboards1, drives1, budget1)); // Output should be 9
    System.out.println(getMoneySpent_v2(keyboards1, drives1, budget1)); // Output should be 9

    int[] keyboards2 = {4};
    int[] drives2 = {5};
    int budget2 = 5;
    System.out.println(getMoneySpent_v1(keyboards2, drives2, budget2)); // Output should be -1
    System.out.println(getMoneySpent_v2(keyboards2, drives2, budget2)); // Output should be -1
  }
}
