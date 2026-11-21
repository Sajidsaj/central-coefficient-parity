"""Independent parity formula for a_w(n) = central coefficient of (1+x+...+x^(w-1))^n.

a_w(n) = sum_j (-1)^j C(n,j) C(n-1+h-w*j, n-1),  h = floor((w-1)n/2)   (n >= 1)
Modulo 2 each binomial is decided by Lucas' theorem: C(N,k) is odd iff k & (N-k) == 0.
This does not use any automaton, so it is an independent check of the automata."""

def odd_binom(N, k):
    return k >= 0 and N >= k and (k & (N - k)) == 0

def par_formula(w, n):
    if n == 0:
        return 1
    h = (w - 1) * n // 2
    s = 0
    for j in range(h // w + 1):
        if odd_binom(n, j) and odd_binom(n - 1 + h - w * j, n - 1):
            s ^= 1
    return s

def central_coefficient(w, n):
    """exact value of a_w(n) (slow for big n)"""
    from math import comb
    if n == 0:
        return 1
    h = (w - 1) * n // 2
    return sum((-1) ** j * comb(n, j) * comb(n - 1 + h - w * j, n - 1) for j in range(h // w + 1))
