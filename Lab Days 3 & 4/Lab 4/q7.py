# Problem Statement:
# Given a list of activities with their start and finish times, select the 
# maximum number of activities with the minimum total duration

def max_activities_min_duration(activities):
    # Sort activities by their durations (finish time - start time)
    activities.sort(key=lambda x: x[1] - x[0])
    
    # Initialize variables
    count = 0  # Count of selected activities
    end_time = 0  # End time of the previous selected activity
    
    # Iterate through the sorted activities
    for start_time, finish_time in activities:
        # If the start time of the current activity is after or equal to the end time of the previous selected activity
        if start_time >= end_time:
            # Increment the count of selected activities
            count += 1
            # Update the end time of the previous selected activity
            end_time = finish_time
    
    return count

activities = [(1, 3), (2, 5), (4, 6), (7, 9), (8, 10)]
print("Maximum Number of Activities:", max_activities_min_duration(activities))
