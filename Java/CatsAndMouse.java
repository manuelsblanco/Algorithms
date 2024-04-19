public class CatAndMouse {

    // Method to determine which cat will catch the mouse first
    public static String catAndMouse(int x, int y, int z) {
        // Calculate the distance between Cat A and the mouse
        int distanceA = Math.abs(x - z);
        // Calculate the distance between Cat B and the mouse
        int distanceB = Math.abs(y - z);

        // Compare the distances to determine which cat is closer to the mouse
        if (distanceA < distanceB) {
            return "Cat A"; // If Cat A is closer, return "Cat A"
        } else if (distanceA > distanceB) {
            return "Cat B"; // If Cat B is closer, return "Cat B"
        } else {
            return "Mouse C"; // If both cats are equidistant, return "Mouse C"
        }
    }

    public static void main(String[] args) {
        // Examples of using the catAndMouse method with input values
        System.out.println(catAndMouse(1, 2, 3)); // Output should be "Cat B"
        System.out.println(catAndMouse(1, 3, 2)); // Output should be "Cat A"
    }
}
