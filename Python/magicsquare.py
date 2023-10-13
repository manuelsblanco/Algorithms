"""
Problem Statement:
We define a magic square to be an n x n matrix of distinct positive integers from 1 to n^2
where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

You will be given an n x n matrix s of integers in the inclusive range [1, n^2].
We can convert any digit a to any other digit b in the range [1, n^2] at a cost of |a - b|.
Given s, convert it into a magic square at minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range [1, n^2].

Example:
s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
The matrix looks like this:
5 3 4
1 5 8
6 4 2
We can convert it to the following magic square:
8 3 4
1 5 9
6 7 2
This took three replacements at a cost of 7.

Function Description:
Complete the formingMagicSquare function below.
formingMagicSquare has the following parameter(s):
- int s[n][n]: an n x n array of integers
Returns
- int: the minimal total cost of converting the input square to a magic square

Input Format:
Each of the n lines contains n space-separated integers of row i.

Constraints:
- 1 <= n <= 15
- 1 <= s[i][j] <= n^2

Sample Input:
4 9 2
3 5 7
8 1 5

Sample Output:
1

Explanation:
If we change the bottom right value, 5, from 5 to 6 at a cost of 1, the matrix becomes a magic square at the minimum possible cost.

Sample Input:
4 8 2
4 5 7
6 1 6

Sample Output:
4
"""


# Complete the formingMagicSquare function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.

def formingMagicSquare(s):
    min_cost = float('inf')

    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    for magic_square in magic_squares:
        cost = 0
        for i in range(len(s)):
            for j in range(len(s[0])):
                cost += abs(s[i][j] - magic_square[i][j])
        min_cost = min(min_cost, cost)

    return min_cost


if __name__ == '__main__':
    n = int(input().strip())
    s = []

    for _ in range(n):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)
