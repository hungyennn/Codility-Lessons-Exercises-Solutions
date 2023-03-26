"""
Question description: https://app.codility.com/programmers/trainings/4/tree_height/
"""
# Total Score: 100%

from extratypes import Tree  # library with types used in the task

def solution(T):
    if T.l == None and T.r == None: return 0
    elif T.l == None: return solution(T.r) + 1
    elif T.r == None: return solution(T.l) + 1
    else: return max(solution(T.r), solution(T.l)) + 1