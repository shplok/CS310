# Problem Statement:
# Given arrival and departure times of trains 
# on a railway platform, find the minimum number of platforms 
# required to accommodate all the trains

def min_platforms(arrival, departure):
    # Sort arrival and departure times
    arrival.sort()
    departure.sort()
    
    platforms_needed = 0
    max_platforms_needed = 0
    i = j = 0
    
    # Iterate through arrival and departure times simultaneously
    while i < len(arrival) and j < len(departure):
        # If a train arrives before the departure of the previous train
        if arrival[i] < departure[j]:
            platforms_needed += 1
            i += 1
            # Update the maximum platforms needed if the current count is greater
            max_platforms_needed = max(max_platforms_needed, platforms_needed)
        else:
            platforms_needed -= 1
            j += 1
    
    return max_platforms_needed

arrival_times = [900, 940, 950, 1100, 1500, 1800]
departure_times = [910, 1200, 1120, 1130, 1900, 2000]
print("Minimum Platforms Required:", min_platforms(arrival_times, departure_times))
