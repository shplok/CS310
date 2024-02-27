def hanoi(n, from_rod, to_rod, helper_rod):



    if n == 0:
        return
    
    hanoi(n-1, from_rod, helper_rod, to_rod)
    
    print("Disk " + str(n) + " moved from rod " + from_rod + " to rod " + to_rod)
    hanoi(n-1, helper_rod, to_rod, from_rod)
    


def main():
    n = int(input("Provide the number of disks: "))
    hanoi(n, 'A', 'B', 'C')
    
    


if __name__ == '__main__':
    main()
