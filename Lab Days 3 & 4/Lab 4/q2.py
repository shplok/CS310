# Problem Statement:
# You are given a list of activities with their start and finish times. you need to select the max # of activities
# that can be performed by a single person, assuming that a person can only work on one activity at a time

# Sample input: Activities: [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]

# sort the activies by finishing time


def max_activites(activities):
    # Sort activities by their end times
    activities.sort(key=lambda x: x[1])
    # Initialize count to track the maximum number of activities
    count = 1
    # Initialize the end time of the first activity
    prev_end_time = activities[0][1]

    # Iterate over the sorted activities starting from the second one
    for start_time, end_time in activities[1:]:
        # If the start time of the current activity is after or equal to the end time of the previous activity
        if start_time >= prev_end_time:
            # Increment the count of compatible activities
            count += 1
            # Update the end time of the previous activity to the end time of the current activity
            prev_end_time = end_time
    
    # Return the maximum number of compatible activities
    return count


activities = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
print(max_activites(activities))
