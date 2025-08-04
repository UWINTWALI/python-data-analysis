import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

all_walks = []

for i in range(500):
    random_walk = [0]

    for step_num in range(100):
        current_floor = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            next_floor = max(0, current_floor - 1)
        elif dice <= 5:
            next_floor = current_floor + 1
        else:
            next_floor = current_floor + np.random.randint(1, 7)

        random_walk.append(next_floor)

    all_walks.append(random_walk)

np_all_walks = np.transpose(np.array(all_walks))
final_floors = np_all_walks[-1, :]
reached_60 = final_floors[final_floors >= 60]
chance_to_reach_60 = len(reached_60) / 500 * 100

print(f"Chance to reach 60th floor: {chance_to_reach_60}%")


def most_frequent_numbers(arr):
    values, counts = np.unique(arr, return_counts=True)
    max_count = np.max(counts)
    return values[counts == max_count]

print("most freq: ", most_frequent_numbers(final_floors))

# Plot histogram of ends, display plot
plt.hist(final_floors, bins=40, color="#66ccff", edgecolor="black")

plt.xlabel("Final foor Level")
plt.ylabel("Journey made")
plt.title("Final Floor Distribution After 500 Random Walks")
plt.show()