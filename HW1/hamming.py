# 1. Write a function that takes the binary representation of an unsigned integer and returns 
# the number of '1' bits in the number (Hamming weight).

# Compare a sequential algorithm to a divide and conquer algorithm.




def hammingSequential(n):

    count = 0
    while(n):
        count += n & 1
        # shift n to the right 1
        n >>= 1

    return count



def hammingDivide(n):

    if n == 0:
        return 0
    else: 
        return (n & 1) + hammingDivide(n >> 1)

def main():
    n = int(input("Please provide an integer for calculation: "))

    seqOrdiv = (input("specify 'Sequential' or 'Divide and Conquer' Method: "))

    if seqOrdiv.lower() == 'sequential' : 
        result = hammingSequential(n)
    if seqOrdiv.lower() == 'divide and conquer':
        result = hammingDivide(n)
    print(result)

if __name__ == '__main__':
    main()


    # In java, the function is essentially the same, the only thing that is worth nothing would be
    # the fact that java just takes way more work to accomplish the same task.