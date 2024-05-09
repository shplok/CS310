def numSquares(n: int) -> int:
    # Generate a list of perfect square numbers less than or equal to n
    squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
    # Set to store visited numbers to avoid duplicate calculations
    visited = set()
    # Queue to perform BFS, each element is a tuple (remaining number, level)
    # where level represents the number of perfect square numbers used so far
    queue = [(n, 0)]
    
    # Perform BFS
    while queue:
        # Pop the front element from the queue
        num, level = queue.pop(0)
        # Iterate through the perfect square numbers
        for square in squares:
            # If the remaining number after subtracting the square is 0, we found the solution
            if num - square == 0:
                return level + 1  # Return the current level + 1 (since we found a perfect square)
            # If the remaining number after subtracting the square is negative, move to the next square
            elif num - square < 0:
                break
            # If the remaining number after subtracting the square is positive and not visited,
            # add it to the queue along with the current level + 1
            if num - square not in visited:
                visited.add(num - square)  # Mark the number as visited
                queue.append((num - square, level + 1))  # Add to the queue with updated level
    
    # If no solution is found, return -1
    return -1

n = 12
print("Least number of perfect squares which sum to", n, "is:", numSquares(n))
# Output: 3
