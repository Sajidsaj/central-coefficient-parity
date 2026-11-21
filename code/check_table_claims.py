"""Checks of the structural claims in docs/PARITY_AUTOMATA.md (inclusions, powers of 2, w = 6 recurrence)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from automata import build, accepts
from lucas_parity import central_coefficient

# S_w for even w <= 40, n < 2^14
N = 1 << 14
S = {}
for w in range(2, 41, 2):
    a = build(w); S[w] = frozenset(n for n in range(N) if accepts(a, n))
ws = sorted(S)
inc = {w: [v for v in ws if v != w and S[w] <= S[v]] for w in ws}
found = {w: v for w, v in inc.items() if v}
claimed = {2: [6, 10, 14, 18, 22, 26, 30, 34, 38], 4: [12, 20, 28, 36], 8: [24, 40]}
assert found == claimed, found
print("inclusions S_a in S_b (a != b), even w <= 40, n < 2^14: exactly", claimed)
common = set(range(N))
for w in ws: common &= S[w]
assert sorted(common) == [0, 1]; print("intersection of all S_w (even w <= 40): [0, 1]")

# powers of two: k+2 states and language 1(0^(k-1)1)*
for k in range(1, 6):
    w = 2 ** k; a = build(w); rx = re.compile(r"^1(0{%d}1)*$" % (k - 1))
    assert a[3] == k + 2
    assert all((n == 0 or bool(rx.match(bin(n)[2:]))) == accepts(a, n) for n in range(N))
print("w = 2^k (k=1..5): k+2 states and language 1(0^(k-1)1)*: OK")

# w = 6: listed terms, recurrence, exact-integer parity
a6 = build(6)
odd6 = [n for n in range(100) if accepts(a6, n)]
assert odd6[:18] == [0, 1, 3, 7, 11, 15, 19, 23, 27, 31, 39, 47, 51, 55, 59, 63, 79, 91]
f = [sum(1 for n in range(1 << (k - 1), 1 << k) if accepts(a6, n)) for k in range(1, 19)]
assert all(f[i] == f[i - 1] + f[i - 3] + f[i - 4] for i in range(4, len(f)))
assert all((central_coefficient(6, n) % 2 == 1) == accepts(a6, n) for n in range(1501))
print("w = 6: listed terms, f(m)=f(m-1)+f(m-3)+f(m-4), exact-integer parity n <= 1500: OK")
print("ALL TABLE CLAIMS PASSED")
