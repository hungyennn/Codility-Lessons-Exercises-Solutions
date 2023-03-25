"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

    S is empty;
    S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
    S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [0..200,000];
    string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
"""

# Total Score: 100%
# Detected time complexity: O(N)

def solution(S):
    
    if len(S) > 200000 or len(S) % 2 != 0: return 0
    
    pair = {'(':')', '[':']', '{':'}'}
    stack = []

    for i in S:
        if i not in ['(', ')', '[', ']', '{', '}']:
            return 0

        if i in pair:
            stack.append(i)
            
        elif len(stack) == 0 or pair[stack.pop()] != i:
            return 0 


    return 1 if not len(stack) else 0