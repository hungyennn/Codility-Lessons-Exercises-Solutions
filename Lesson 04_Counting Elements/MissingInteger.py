"""
Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, 
Given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

# Total Score: 100%
# Detected time complexity: O(N) or O(N * log(N))

def solution(A):
    lenA = len(A)
    ls = [0] * (lenA + 2)

    for i in A:
        if 1 <= i <= lenA:
            ls[i] += 1
    for j in range(1, lenA + 2):
        if ls[j] == 0: return j