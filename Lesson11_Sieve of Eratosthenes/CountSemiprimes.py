"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. 
The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. 
The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. 
These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), 
where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

The number of semiprimes within each of these ranges is as follows:

    (1, 26) is 10,
    (4, 10) is 4,
    (16, 20) is 0.

Write a function:

    def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, 
returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..50,000];
    M is an integer within the range [1..30,000];
    each element of arrays P and Q is an integer within the range [1..N];
    P[i] ≤ Q[i].
"""
# Total Score: 100%
# Detected time complexity: O(N * log(log(N)) + M)

def primeSieve(n):
    sieve = [True] * (n + 1) # assume all numbers ( 0 - n) are all prime num
    sieve[0] = sieve[1] = False

    i = 2
    while (i * i <= n):
        if sieve[i]:
            j = i * i
            while (j <= n):
                sieve[j] = False
                j += i
        i += 1
    return sieve


def semiprime(n):
    primesieve = primeSieve(n)
    prime = []

    for i in range(len(primesieve)):
        if primesieve[i]: 
            prime.append(i)

    lenPrime = len(prime)
    semiprime = [False] * (n + 1)

    for j in range(lenPrime):
        if j * j > n:
            break
        
        for k in range(j, lenPrime):
            if prime[k] * prime[j] > n: 
                break
            semiprime[prime[k] * prime[j]] = True

    cntSemiPrime = []
    cnt = 0

    for k in semiprime:
        if k:
            cnt += 1
        cntSemiPrime.append(cnt)
    # print(cntSemiPrime)
    return cntSemiPrime


def solution(N, P, Q):
    cntSemiPrime = semiprime(N)
    res = []
    
    for i in range(len(P)):
        res.append(cntSemiPrime[Q[i]] - cntSemiPrime[P[i] - 1])

    return res