"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

    def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, 
namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..2,147,483,647].
"""

# Total Score: 100%
# Detected time complexity: O(sqrt(N))

def solution(N):
    if N < 1: return 0

    res = 0
    for i in range(1, int(N ** 0.5 + 1)):
        if i ** 2 < N and N % i == 0:
            res += 2
        if i ** 2 == N:
            res += 1
    
    return res