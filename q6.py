import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity, except the start node which is 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to store nodes with their corresponding distances from the start node
    # Each element in the priority queue is a tuple (distance, node)
    pq = [(0, start)]
    
    # Dijkstra's algorithm
    while pq:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # If the current distance is greater than the distance already stored for this node, skip it
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the distance to the neighbor through the current node
            distance = current_distance + weight
            
            # If the new distance is smaller than the previously stored distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Push the neighbor and its updated distance into the priority queue
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Given graph represented as a dictionary
graph = {
    0: {1: 10, 2: 5},
    1: {2: 2, 3: 1},
    2: {1: 3, 3: 9},
    3: {},
    4: {}
}

# Source vertex
source_vertex = 0

# Call Dijkstra's algorithm to find the shortest distances
shortest_distances = dijkstra(graph, source_vertex)

# Print the result
for vertex, distance in shortest_distances.items():
    if distance == float('inf'):
        print("INF")
    else:
        print(distance)
# Output: 0 , 8 , 5 , 9 , INF
