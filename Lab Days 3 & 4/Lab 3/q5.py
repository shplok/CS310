import heapq

def dijkstra(graph, start, end):
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
        
        # If the current node is the destination, return its distance
        if current_node == end:
            return current_distance
        
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
    
    # If the destination node is unreachable, return infinity
    return float('inf')


graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 7, 'E': 4},
    'D': {'E': 2},
    'E': {}
}

source_node = 'A'
destination_node = 'Es'
shortest_distance = dijkstra(graph, source_node, destination_node)

print("Shortest distance from node", source_node, "to node", destination_node + ":", shortest_distance)
