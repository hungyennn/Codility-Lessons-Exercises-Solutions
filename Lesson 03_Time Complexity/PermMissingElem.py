"""
An array A consisting of N different integers is given. 
The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [0..100,000];
    the elements of A are all distinct;
    each element of array A is an integer within the range [1..(N + 1)].
"""

# Total Score: 100%
# Detected time complexity: O(N) or O(N * log(N))

def solution(A):
    
    N = len(A)

    A.sort()
    if N == 1 and A[0] == 1: return 2 # [1]
    if 1 not in A: return 1 

    for i in range(1, N):
        if A[i] - A[i - 1] != 1: # [1, 3, 4, 5] return 2
            return A[i] - 1
        elif i == N-1: # 如果是在最後一個數 [1, 2, 3, 4] return 5 
            return A[i] + 1