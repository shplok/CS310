# Problem Statement:
# Given a set of items, each with a weight and 
# a value, determine the maximum value of fractions of items that 
# can be taken into a knapsack of a certain capacity.

def fractional_knapsack(items, capacity):
    
    
    # Sort the items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    
    # Iterate through the sorted items
    for weight, value in items:
        # If the weight of the current item is less than or equal to the remaining capacity
        if weight <= remaining_capacity:
            # Take the entire item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take a fraction of the current item to fill the remaining capacity
            fraction = remaining_capacity / weight
            total_value += fraction * value
            remaining_capacity = 0
            break  # We have filled the knapsack completely
    
    return total_value

items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
print("Maximum Value:", fractional_knapsack(items, capacity))
