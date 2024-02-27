def maxValIterative(testList):
    if not testList or not any(testList):
        return "No valid elements found"

    max_val = float('-inf')
    for row in testList:
        for val in row:
            if val > max_val:
                max_val = val

    return max_val

def minValIterative(testList):
    if not testList or not any(testList):
        return "No valid elements found"

    min_val = float('inf')
    for row in testList:
        for val in row:
            if val < min_val:
                min_val = val

    return min_val

# include divide and conquer method as well

def main():


    print("Enter the matrix values row-wise, each separated by a space:")

    # Input for the number of rows and columns
    N, M = map(int, input().split())

    # Input for the matrix
    testList = [list(map(int, input().split())) for _ in range(N)]

    max_iter = maxValIterative(testList)
    min_iter = minValIterative(testList)

    print("\nMax value: " + str(max_iter))
    print("Min value: " + str(min_iter) + "\n")

if __name__ == "__main__":
    main()
