# Problem Description:
# Two cats and a mouse are at various positions on a line. 
# You will be given their starting positions. Your task is to determine 
# which cat will catch the mouse first, assuming the mouse does not move 
# and the cats travel at equal speed. If the cats arrive at the same time, 
# the mouse will escape while they fight.
#
# Function Description:
# The function catAndMouse takes the following parameters:
# - int x: Cat A's position
# - int y: Cat B's position
# - int z: Mouse's position
# It returns a string: Either 'Cat A', 'Cat B', or 'Mouse C'
#
# Input Format:
# The first line contains a single integer, q, denoting the number of queries.
# Each of the q subsequent lines contains three space-separated integers 
# describing the respective values of x (Cat A's location), y (Cat B's location), 
# and z (Mouse's location).

def catAndMouse(x, y, z):
    distance_a = abs(x - z)
    distance_b = abs(y - z)

    if distance_a < distance_b:
        return "Cat A"
    elif distance_a > distance_b:
        return "Cat B"
    else:
        return "Mouse C"


# Example usage:
print(catAndMouse(1, 2, 3))  # Output should be "Cat B"
print(catAndMouse(1, 3, 2))  # Output should be "Cat A"
