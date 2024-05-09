from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col, word_index):
            # Base case: If all characters in the word have been matched
            if word_index == len(word):
                return True
            
            # If current position is out of bounds or does not match the current character
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[word_index]:
                return False
            
            # Mark the current cell as visited
            temp, board[row][col] = board[row][col], '#'
            
            # Explore adjacent cells in all four directions
            found = dfs(row+1, col, word_index+1) or dfs(row-1, col, word_index+1) \
                    or dfs(row, col+1, word_index+1) or dfs(row, col-1, word_index+1)
            
            # Restore the current cell
            board[row][col] = temp
            
            return found
        
        # Start DFS from each cell in the grid
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        
        return False


board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word = "ABCCED"
sol = Solution()
print(sol.exist(board, word))
