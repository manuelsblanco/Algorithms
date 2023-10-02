# Problem Statement:
# A person wants to determine the most expensive computer keyboard and USB drive
# that can be purchased with a given budget. Given price lists for keyboards and USB
# drives and a budget, find the cost to buy them. If it is not possible to buy both
# items, return -1.

# Input Format:
# The first line contains three space-separated integers, b, n, and m,
# the budget, the number of keyboard models, and the number of USB drive models.
# The second line contains n space-separated integers, the prices of each keyboard model.
# The third line contains m space-separated integers, the prices of the USB drives.

# Output:
# Return the maximum that can be spent, or -1 if it is not possible to buy both items.

# Solution 1: Using nested loops
def getMoneySpent_v1(keyboards, drives, b):
    total = []
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if (keyboards[i] + drives[j]) <= b:
                total.append(keyboards[i] + drives[j])

    if len(total) > 0:
        total.sort(reverse=True)
        return total[0]
    else:
        return -1


# Solution 2: Using list comprehensions and max()
def getMoneySpent_v2(keyboards, drives, b):
    total = [k + d for k in keyboards for d in drives if k + d <= b]
    return max(total, default=-1)


# Testing the solutions
print(getMoneySpent_v1([3, 1], [5, 2, 8], 10))  # Output should be 9
print(getMoneySpent_v2([3, 1], [5, 2, 8], 10))  # Output should be 9

print(getMoneySpent_v1([4], [5], 5))  # Output should be -1
print(getMoneySpent_v2([4], [5], 5))  # Output should be -1
