# Problem Statement:
# Given a list of activities with their start and finish times, select the 
# maximum number of non-overlapping activities to minimize 
# conflicts

def max_non_overlapping_activities(activities):
    # Sort activities by their finish times
    activities.sort(key=lambda x: x[1])
    
    # Initialize variables
    count = 1  # Count of non-overlapping activities
    prev_finish_time = activities[0][1]  # Finish time of the first activity
    
    # Iterate through the sorted activities starting from the second one
    for start_time, finish_time in activities[1:]:
        # If the start time of the current activity is after or equal to the finish time of the previous activity
        if start_time >= prev_finish_time:
            # Increment the count of non-overlapping activities
            count += 1
            # Update the finish time of the previous activity
            prev_finish_time = finish_time
    
    return count

activities = [(1, 3), (2, 4), (3, 6), (5, 7), (6, 8)]
print("Maximum Number of Activities:", max_non_overlapping_activities(activities))
