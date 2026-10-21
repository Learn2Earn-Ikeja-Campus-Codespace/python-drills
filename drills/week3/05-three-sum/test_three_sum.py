import time
from three_sum import three_sum

part1_total = 0
part1_fail = 0
part2_total = 0
part2_fail = 0


def normalize_triplets(triplets):
    if not isinstance(triplets, list):
        return triplets
    return sorted([sorted(list(t)) for t in triplets])


def check(label, input_list, expected):
    global part1_total, part1_fail
    part1_total += 1
    input_copy = list(input_list)
    got = three_sum(input_list)

    norm_got = normalize_triplets(got)
    norm_expected = normalize_triplets(expected)

    if norm_got != norm_expected:
        part1_fail += 1
        print(f"FAIL [{label}]")
        print(f"  input:    {input_copy!r}")
        print(f"  expected: {expected!r}")
        print(f"  got:      {got!r}\n")


# ── Part 1: Correctness ────────────────────────────────────────────────────────

# examples from spec
check("spec example 1: standard",             [-1, 0, 1, 2, -1, -4],       [[-1, -1, 2], [-1, 0, 1]])
check("spec example 2: three zeros",          [0, 0, 0],                   [[0, 0, 0]])
check("spec example 3: four zeros",           [0, 0, 0, 0],                [[0, 0, 0]])
check("spec example 4: no triplet sum to 0",  [1, 2, -2, -1],              [])
check("spec example 5: multiple valid",       [-2, 0, 1, 1, 2],            [[-2, 0, 2], [-2, 1, 1]])
check("spec example 6: duplicate negatives",  [-1, -1, -1, 2, 2],          [[-1, -1, 2]])
check("spec example 7: no valid triplet",     [3, -2, 1, 0],               [])
check("spec example 8: limited counts",       [-4, -1, -1, 0, 1, 2],       [[-1, -1, 2], [-1, 0, 1]])

# edge cases
check("empty list",                           [],                          [])
check("single element",                       [0],                         [])
check("two elements",                         [-1, 1],                     [])
check("all positive numbers",                 [1, 2, 3, 4, 5],             [])
check("all negative numbers",                 [-5, -4, -3, -2, -1],        [])
check("many zeros",                           [0, 0, 0, 0, 0, 0],          [[0, 0, 0]])
check("duplicate zeros and numbers",          [-2, 0, 0, 2, 2],            [[-2, 0, 2]])
check("already sorted input",                 [-4, -1, -1, 0, 1, 2],       [[-1, -1, 2], [-1, 0, 1]])
check("reverse sorted input",                 [2, 1, 0, -1, -1, -4],       [[-1, -1, 2], [-1, 0, 1]])

# mutation check
orig = [-1, 0, 1, 2, -1, -4]
orig_copy = orig.copy()
res = three_sum(orig)
part1_total += 1
if orig != orig_copy:
    part1_fail += 1
    print("FAIL [does not mutate original list]")
    print(f"  original list was modified: changed from {orig_copy!r} to {orig!r}")
    print("  Hint: avoid in-place numbers.sort(); use sorted(numbers) or sort a copy!\n")

print(f"Part 1 (Correctness): {part1_total - part1_fail}/{part1_total} passed")


# ── Part 2: Algorithmic Efficiency ────────────────────────────────────────────

if part1_fail > 0:
    print("\nPart 2 (Algorithmic Efficiency): skipped (fix Part 1 correctness first)")
else:
    print("\nPart 2 (Algorithmic Efficiency):")

    # Time complexity check: 1,000 items must complete in < 1.0s
    # O(n^2) completes in ~0.15s; O(n^3) brute-force takes > 15s.
    part2_total += 1
    large_list = list(range(-500, 500))
    start_time = time.perf_counter()
    ans_time = three_sum(large_list)
    elapsed = time.perf_counter() - start_time

    if not isinstance(ans_time, list) or len(ans_time) != 124750:
        part2_fail += 1
        print("FAIL [time: large list correctness]")
        print(f"  expected 124750 triplets, got: {len(ans_time) if isinstance(ans_time, list) else ans_time!r}\n")
    elif elapsed > 1.0:
        part2_fail += 1
        print("FAIL [time: O(n^2) requirement]")
        print(f"  took: {elapsed:.2f}s (must finish in < 1.0s; avoid O(n^3) brute force with 3 nested loops)\n")
    else:
        print(f"  [PASS] time complexity: {elapsed:.3f}s (< 1.0s, O(n^2) two-pointer verified)")

    print(f"\nPart 2 result: {part2_total - part2_fail}/{part2_total} passed")

    if part2_fail == 0:
        print("\nBIM!!!")
    else:
        print("\nDrill incomplete: Part 2 efficiency requirements must pass to finish this drill.")
