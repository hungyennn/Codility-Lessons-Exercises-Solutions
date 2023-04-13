"""
A non-empty array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [1..1,000,000,000].
"""

# Total Score: 100%
# Detected time complexity: O(N) or O(N * log(N))

def solution(A):
    # Implement your solution here
    from collections import Counter
    counter = Counter(A)
    if len(counter) != max(counter): return 0 # if max = 4, len = 4  

    for i, v in dict(counter).items():
        if v > 1: return 0 # assure that every number appears 1 time 
    
    return 1 