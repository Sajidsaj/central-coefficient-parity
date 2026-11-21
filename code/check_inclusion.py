"""Checks supporting PROOF_inclusion.md: S_{2^s} is contained in S_{2^s m} for odd m >= 3."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from functools import lru_cache
from lucas_parity import par_formula
from automata import build

def T_parity_gf(w, m, j):
    """parity of #{(e_0..e_{j-1}) in [0,m-1]^j : sum e_t w^t = Q}; polynomials over GF(2) as Python ints"""
    n = (w ** j - 1) // (w - 1)
    Q = ((m - 1) * n - w ** (j - 1)) // 2
    poly = 1
    for t in range(j):
        acc = 0
        for e in range(m): acc ^= poly << (e * w ** t)
        poly = acc
    return (poly >> Q) & 1

# Step 1-3 of the proof: a_{wm}(n_j) == 1 + T (mod 2)
tested = 0
for w in (2, 4, 8):
    for m in (3, 5, 7, 9):
        for j in (2, 3):
            n = (w ** j - 1) // (w - 1)
            if w * m > 60 or n > 3000: continue
            assert par_formula(w * m, n) == (1 + T_parity_gf(w, m, j)) & 1
            tested += 1
print("a_{wm}(n_j) = 1 + T (mod 2):", tested, "cases OK")

# T is even for w = 2^s (this is what Step 4 proves); numerical confirmation on a wide range
cases = 0
for w in (2, 4, 8, 16, 32):
    for m in range(3, 152, 2):
        for j in range(2, 9):
            n = (w ** j - 1) // (w - 1)
            if (m - 1) * n > 3000000: continue
            assert T_parity_gf(w, m, j) == 0, (w, m, j)
            cases += 1
print("T even: %d cases (w = 2,4,8,16,32; odd m <= 151; j = 2..8) OK" % cases)

# Step 4: the involution works on explicit solution sets
def solutions(w, m, j):
    r = (m - 1) // 2; N = w ** (j - 1) // 2; out = []
    def rec(t, rem, acc):
        if t == j:
            if rem == 0: out.append(tuple(acc))
            return
        for d in range(-r, r + 1):
            if (rem - d) % w == 0: rec(t + 1, (rem - d) // w, acc + [d])
    rec(0, N, []); return out
cases = total = 0
for w in (2, 4, 8, 16):
    for m in range(3, 24, 2):
        for j in range(2, 5):
            if m ** j > 300000: continue
            S = set(solutions(w, m, j)); r = (m - 1) // 2
            assert len(S) % 2 == 0
            for d in S:
                e = tuple(-x for x in d[:-1]) + (1 - d[-1],)
                assert e in S and e != d and max(abs(x) for x in e) <= r
            cases += 1; total += len(S)
print("involution: %d parameter cases, %d solutions, all pairs fixed-point-free: OK" % (cases, total))

# Direct parity check of the final statement for w = 2: a_{2m}(2^j - 1) is odd
pairs = 0
for m in range(3, 40, 2):
    for j in range(1, 11):
        assert par_formula(2 * m, 2 ** j - 1) == 1, (m, j); pairs += 1
print("direct parity check a_{2m}(2^j-1) odd: %d pairs (odd m <= 39, j = 1..10) OK" % pairs)

# Final statement for specific (w,m): language 1(0^{s-1}1)* is inside the odd set of w*m (finite automaton check)
pairs = 0
for w, ms in ((2, range(3, 24, 2)), (4, (3, 5, 7, 9, 11)), (8, (3, 5, 7)), (16, (3,))):
    s = w.bit_length() - 1
    for m in ms:
        S0, mt, macc, M = build(w * m)
        st = mt[(S0, 1)]; assert st in macc
        seen = set()
        while st not in seen:
            seen.add(st)
            for b in [0] * (s - 1) + [1]: st = mt[(st, b)]
            assert st in macc
        pairs += 1
print("automaton check of the inclusion: %d pairs (w, m) OK" % pairs)
print("ALL INCLUSION CHECKS PASSED")
