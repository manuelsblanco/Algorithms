import heapq


def dijkstra(graph, start):
    # Create a priority queue to store (distance, vertex) pairs
    pq = []

    # Dictionary to store the shortest distance to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Push the starting vertex onto the queue with distance 0
    heapq.heappush(pq, (0, start))

    while pq:
        # Pop the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(pq)

        # If the popped distance is greater than the current recorded distance, skip
        if current_distance > distances[current_vertex]:
            continue

        # Explore the neighbors of the current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update the distance and push it onto the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(f"Shortest distances from {start_vertex}: {distances}")
