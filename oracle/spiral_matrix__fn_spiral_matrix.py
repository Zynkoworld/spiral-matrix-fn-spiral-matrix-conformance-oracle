"""spiral-matrix-fn-spiral-matrix-conformance-oracle -- deterministic CONFORMANCE oracle for `spiral-matrix` (python).

WHAT THIS DECIDES: given a candidate callable and one canonical input, it decides whether the candidate
agrees with the proven reference. It is a *conformance* decider over a fixed, published corpus -- it does
not decide correctness in general, and it says nothing about inputs outside the corpus.

SCOPE (declared, so the boundary is visible rather than discovered): the corpus is the canonical Exercism
test data for this task, 6 input/output pairs, listed in `probes/probes.jsonl`. Inputs outside that
set are simply not covered; `decide` answers only about the input it is given.

PROVENANCE: the reference body comes from the Exercism reference solution for `spiral-matrix` (MIT, Exercism);
the type annotations were added by harvest, the body is unchanged (checked at AST level). The capability
was PROVEN by the exercism testsuite (pin=dee0c4ebcdb61ba3) and re-executed by harvest in a sealed sandbox
(unshare -rn) -- verify-not-relay, not a copied ledger label.
"""

TASK = "spiral-matrix"
CWE = "spiral-matrix"          # a publish-motor egyseges mezonevet var; itt a feladat azonositoja


def decide(fn, value, expect):
    """PASS iff fn(value) == expect. Determinista, nincs halozat, nincs allapot."""
    try:
        return "PASS" if fn(value) == expect else "FAIL"
    except Exception:                                      # noqa: BLE001
        return "FAIL"


def spiral_matrix(size: int) -> list:
    matrix = [[0] * size for row in range(size)]
    idx = 0
    jdx = -1
    element = 1
    digital = [0, 1, 0, -1]
    disco = [1, 0, -1, 0]
    for edx in range(2 * size - 1):
        for _ in range((2 * size - edx) // 2):
            idx += digital[edx % 4]
            jdx += disco[edx % 4]
            matrix[idx][jdx] = element
            element += 1
    return matrix

REFERENCE = spiral_matrix
