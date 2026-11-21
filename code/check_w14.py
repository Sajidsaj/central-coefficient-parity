"""Checks of the facts used in the OEIS entries for w = 14 (central coefficient of (1+...+x^13)^n)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from collections import Counter
import numpy as np, sympy as sp
from automata import build, accepts, trim, growth
from lucas_parity import par_formula, central_coefficient

HERE = os.path.dirname(__file__)
auto = build(14)
S0, mt, macc, m = auto
print("minimal DFA states:", m, "(expected 23)")
assert m == 23

# 1. automaton vs independent Lucas parity
bad = [n for n in range(30001) if accepts(auto, n) != bool(par_formula(14, n))]
print("automaton vs independent parity, n<=30000, mismatches:", len(bad)); assert not bad

# 2. data files agree
b = [tuple(map(int, l.split())) for l in open(os.path.join(HERE, "..", "data", "b_w14.txt"))]
assert all(central_coefficient(14, n) == v for n, v in b[:120])
print("b_w14.txt first 120 terms agree with the sum formula")
odd = [int(l.split()[1]) for l in open(os.path.join(HERE, "..", "data", "b_odd14.txt"))]
assert odd[:2000] == [n for n in range(0, 100000) if accepts(auto, n)][:2000]
print("b_odd14.txt first 2000 terms agree with the automaton")

# 3. structural facts, as finite checks on the automaton
SINK = [s for s in range(m) if mt[(s, 0)] == s and mt[(s, 1)] == s and s not in macc][0]
def run(s, w):
    for ch in w: s = mt[(s, int(ch))]
    return s
reach = {mt[(S0, 1)]}; todo = [mt[(S0, 1)]]
while todo:
    s = todo.pop()
    for bit in (0, 1):
        t = mt[(s, bit)]
        if t not in reach: reach.add(t); todo.append(t)
for f in ("0000", "01000", "10010"):
    assert all(run(s, f) == SINK for s in reach); print("factor", f, "leads to the dead state from every state: OK")
accr = [s for s in reach if s in macc]
for suf in ("111", "0011", "0111"):
    assert all(run(s, suf) in macc for s in accr)
    print("appending", suf, "keeps membership (n -> 2^%d n + %d): OK" % (len(suf), int(suf, 2)))
L = [n for n in range(1 << 15) if accepts(auto, n)]
assert all(n in (0, 1) or n % 4 == 3 for n in L); print("every term > 1 is 3 mod 4 (n < 2^15): OK")
st = mt[(S0, 1)]; assert st in macc and mt[(st, 1)] == st; print("1^k stays accepting: all 2^k-1 are terms: OK")

# 4. growth
lam, tn = growth(auto)
print("dominant eigenvalue %.8f, exponent log2 = %.5f" % (lam, np.log2(lam)))
cnt = [sum(1 for n in range(1 << (k - 1), 1 << k) if accepts(auto, n)) for k in range(1, 17)]
print("terms with exactly k binary digits, k=1..16:", cnt)
assert cnt == [1, 1, 1, 1, 3, 5, 8, 12, 24, 38, 66, 108, 195, 319, 543, 915]
print("ALL w=14 CHECKS PASSED")
