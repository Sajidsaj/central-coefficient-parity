"""w = 6: a_6(n) is odd iff n = 0 or the binary expansion of n lies in 1{1,011,0011}*."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from automata import build, accepts
from lucas_parity import par_formula
auto = build(6)
rx = re.compile(r"^1(1|011|0011)*$")
bad = [n for n in range(1, 1 << 16) if bool(rx.match(bin(n)[2:])) != accepts(auto, n)]
print("regex vs automaton, n < 2^16, mismatches:", len(bad)); assert not bad
bad = [n for n in range(0, 20001) if accepts(auto, n) != bool(par_formula(6, n))]
print("automaton vs independent parity, n <= 20000, mismatches:", len(bad)); assert not bad
print("ALL w=6 CHECKS PASSED")
