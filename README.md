# Parity of central coefficients of (1 + x + ... + x^(w-1))^n

Unrefereed research notes with all supporting computations. Author: Sajid Khan Hussain.

Let `a_w(n)` be the central (largest) coefficient of `(1 + x + ... + x^(w-1))^n`
(OEIS [A077042](https://oeis.org/A077042) row `w`; A402341 is `w = 16`, A402403 is `w = 14`).
This repository studies **when `a_w(n)` is odd**.

## Results and their status

| Statement | Status |
|---|---|
| `w` odd: `a_w(n)` is odd for every `n` | Proved (symmetry of the coefficients) |
| `w = 2^k`: `a_w(n)` odd iff `n = (w^j - 1)/(w - 1)` | Proved (mod 2 reduction and Lucas' theorem) |
| For every even `w`, `a_w(n) mod 2` is computed by a finite automaton reading `n` in binary | Proved (hand-derived recursion, automata built and checked by computer) |
| `w = 6`: `a_6(n)` odd iff `n = 0` or `bin(n)` is in `1{1,011,0011}*` | Proved (computer-assisted, from the 6-state automaton); checked against an independent formula for `n <= 20000` |
| `w = 14`: odd terms are `0`, `1` or `n == 3 (mod 4)`; no factors `0000`, `01000`, `10010` in binary; closed under `k -> 8k+7, 16k+3, 16k+7` | Proved (computer-assisted, finite check on the 23-state automaton) |
| `S_{2^s}` is contained in `S_{2^s m}` for every `s >= 1`, odd `m >= 3` (`S_w` = `{n : a_w(n) odd}`) | Proved by hand (see `docs/PROOF_inclusion.md`), plus numerical checks; **not refereed** |
| Growth `~ N^0.762` of the odd set for `w = 14`; table of automaton sizes and growth rates for even `w` | Computed |
| For `w = 6*2^s` the minimal automaton has `7*2^s - 1` states; `lambda(m*2^s)` mostly decreases as `s` grows (not for `m = 7`, `s = 0 -> 1`) | Observation only (data), not proved |

Nothing here is claimed to be new. A general theorem (Rowland and Yassawi, arXiv:1310.8635) already gives that such
sequences are automatic mod `p`; we only did not find the explicit statements above in the sources we checked
(a limited search; OEIS term search and the main databases were not available to us).

## Layout
- `docs/PROOF_inclusion.md` the inclusion proof
- `docs/PARITY_AUTOMATA.md` notes, table, literature check
- `code/automata.py` builds the parity automaton for any `w`; `code/lucas_parity.py` independent parity formula
- `code/check_w6.py`, `code/check_w14.py`, `code/check_inclusion.py`, `code/check_table_claims.py`, `code/table.py`; `code/run_all.py` runs the first four
- `code/check_even_w.py` slower extra check (all even `w <= 48`, about 2 minutes), not part of `run_all.py`
- `data/` b-files for OEIS A402403 (`b_w14.txt`) and for the sequence "n such that a_14(n) is odd" (`b_odd14.txt`)

## Run
```
pip install -r requirements.txt
python code/run_all.py        # about 2 minutes
python code/table.py 30       # table for even w <= 30
```

## Licence
Text and data: CC BY 4.0 (`LICENSE`). Code: MIT (`LICENSE-CODE`).
