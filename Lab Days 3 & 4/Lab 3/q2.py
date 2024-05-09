from collections import deque  # Importing deque from collections module

def is_valid_move(maze, row, col):
    # Function to check if the move (row, col) is valid within the maze
    rows = len(maze)  # Get the number of rows in the maze
    cols = len(maze[0])  # Get the number of columns in the maze
    # Check if the move is within the bounds of the maze and the cell is not blocked (maze[row][col] == 1)
    return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 1

def shortestPath(maze, start, destination):
    if maze[start[0]][start[1]] == 0 or maze[destination[0]][destination[1]] == 0:
        # Check if either the start or destination cell is blocked
        return -1  # If either is blocked, return -1 indicating no valid path
    
    rows = len(maze)  # Get the number of rows in the maze
    cols = len(maze[0])  # Get the number of columns in the maze
    visited = [[False] * cols for _ in range(rows)]  # Initialize a 2D array to keep track of visited cells
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Define possible directions: down, up, right, left
    
    queue = deque([(start[0], start[1], 0)])  # Initialize a queue for BFS traversal with starting cell and distance 0
    visited[start[0]][start[1]] = True  # Mark the starting cell as visited
    
    while queue:  # Perform BFS traversal until the queue is empty
        row, col, distance = queue.popleft()  # Dequeue the cell and its distance from the queue
        
        if (row, col) == destination:
            # If the dequeued cell is the destination cell, return the distance
            return distance  # We've found the shortest path to the destination
        
        for dr, dc in directions:
            # Iterate over the possible directions
            new_row, new_col = row + dr, col + dc  # Calculate the new row and column indices
            
            while is_valid_move(maze, new_row, new_col):
                # While the move in the current direction is valid
                if not visited[new_row][new_col]:
                    # If the new cell has not been visited yet
                    visited[new_row][new_col] = True  # Mark the new cell as visited
                    queue.append((new_row, new_col, distance + 1))  # Enqueue the new cell with updated distance
                new_row += dr  # Move to the next cell in the current direction
                new_col += dc
            
    return -1  # If no valid path is found, return -1

# Define the maze as a 2D list of integers (0 for blocked, 1 for open)
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1]
]

start = (0, 0)  # Define the starting cell
destination = (3, 4)  # Define the destination cell

# Call the shortestPath function with the maze, starting cell, and destination cell
print("Shortest path length:", shortestPath(maze, start, destination))  # Print the shortest path length
