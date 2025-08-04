# Import NumPy and set a fixed random seed for reproducibility
import numpy as np
np.random.seed(123)

# List to store all the random walk journeys
all_walks = []

# Simulate 500 random walk journeys (500 separate simulations)
for i in range(500):
    random_walk = [0]  # Start each journey at floor 0

    for step_num in range(100):  # Each journey has 100 steps
        current_floor = random_walk[-1]  # Get the last floor you're on
        dice = np.random.randint(1, 7)   # Roll a six-sided die

        if dice <= 2:
            # You slip down 1 floor, but never below floor 0
            next_floor = max(0, current_floor - 1)
        elif dice <= 5:
            # Normal step up: move up 1 floor
            next_floor = current_floor + 1
        else:
            # Magic elevator: randomly jump ahead 1 to 6 floors
            next_floor = current_floor + np.random.randint(1, 7)

        # Add the new floor to your journey
        random_walk.append(next_floor)

    # After one full journey, store it in the all_walks list
    all_walks.append(random_walk)

# Convert the list of all journeys into a NumPy array and transpose it
# So that each row represents a step number and each column a full journey
np_all_walks = np.transpose(np.array(all_walks))

# Look at the final floor reached in each journey (last row)
final_floors = np_all_walks[-1, :]

# Count how many journeys ended at floor 60 or above
reached_60 = final_floors[final_floors >= 60]

# Calculate the percentage chance of reaching at least floor 60
chance_to_reach_60 = len(reached_60) / 5 * 100

# Output the result
print(f"Chance to reach 60th floor: {chance_to_reach_60}%")
