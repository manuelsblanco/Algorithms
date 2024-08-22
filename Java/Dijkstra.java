import java.util.*;

public class Dijkstra {

    // Method to implement Dijkstra's algorithm
    public static Map<String, Integer> dijkstra(Map<String, List<Node>> graph, String start) {
        // Priority queue to store (distance, vertex) pairs
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.distance));

        // Map to store the shortest distance to each vertex
        Map<String, Integer> distances = new HashMap<>();
        for (String vertex : graph.keySet()) {
            distances.put(vertex, Integer.MAX_VALUE);
        }
        distances.put(start, 0);

        // Add the start vertex to the queue
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            // Extract the vertex with the smallest distance
            Node currentNode = pq.poll();
            String currentVertex = currentNode.vertex;
            int currentDistance = currentNode.distance;

            // If the extracted distance is greater than the current recorded distance, skip
            if (currentDistance > distances.get(currentVertex)) {
                continue;
            }

            // Explore the neighbors of the current vertex
            for (Node neighbor : graph.get(currentVertex)) {
                int newDist = distances.get(currentVertex) + neighbor.distance;

                // If a shorter path to the neighbor is found, update the distance and add it to the queue
                if (newDist < distances.get(neighbor.vertex)) {
                    distances.put(neighbor.vertex, newDist);
                    pq.add(new Node(neighbor.vertex, newDist));
                }
            }
        }

        return distances;
    }

    // Node class to represent a vertex and its distance
    static class Node {
        String vertex;
        int distance;

        Node(String vertex, int distance) {
            this.vertex = vertex;
            this.distance = distance;
        }
    }

    // Main method to test Dijkstra's algorithm
    public static void main(String[] args) {
        // Example graph represented as an adjacency list
        Map<String, List<Node>> graph = new HashMap<>();
        graph.put("A", Arrays.asList(new Node("B", 1), new Node("C", 4)));
        graph.put("B", Arrays.asList(new Node("A", 1), new Node("C", 2), new Node("D", 5)));
        graph.put("C", Arrays.asList(new Node("A", 4), new Node("B", 2), new Node("D", 1)));
        graph.put("D", Arrays.asList(new Node("B", 5), new Node("C", 1)));

        // Run Dijkstra's algorithm
        String startVertex = "A";
        Map<String, Integer> distances = dijkstra(graph, startVertex);

        // Print the shortest distances from the start vertex
        System.out.println("Shortest distances from " + startVertex + ":");
        for (Map.Entry<String, Integer> entry : distances.entrySet()) {
            System.out.println("Vertex " + entry.getKey() + ": " + entry.getValue());
        }
    }
}
