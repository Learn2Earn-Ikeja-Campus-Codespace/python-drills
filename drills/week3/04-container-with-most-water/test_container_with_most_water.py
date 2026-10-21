import time
import tracemalloc

try:
    from container_with_most_water import max_area
except ImportError:
    try:
        from container_with_most_water import container_with_most_water as max_area
    except ImportError:
        raise ImportError("Could not import max_area or container_with_most_water from container_with_most_water.py")

part1_total = 0
part1_fail = 0
part2_total = 0
part2_fail = 0


def check(label, input_list, expected):
    global part1_total, part1_fail
    part1_total += 1
    input_copy = list(input_list)
    got = max_area(input_list)
    if got != expected:
        part1_fail += 1
        print(f"FAIL [{label}]")
        print(f"  expected: {expected!r}")
        print(f"  got:      {got!r}\n")


# ── Part 1: Correctness ────────────────────────────────────────────────────────

# examples from spec
check("spec example 1: standard",             [1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
check("spec example 2: two equal lines",       [1, 1],                       1)
check("spec example 3: peak in middle",        [1, 2, 1],                    2)
check("spec example 4: equal boundaries",      [4, 3, 2, 1, 4],              16)
check("spec example 5: best pair inside",      [1, 2, 4, 3],                 4)
check("spec example 6: all heights equal",     [5, 5, 5, 5],                 15)
check("spec example 7: interior tall lines",   [2, 3, 10, 5, 7, 8, 9],       36)

# edge cases
check("empty list",                           [],                           0)
check("single line",                          [5],                          0)
check("zero height on boundary",              [0, 2],                       0)
check("all zeros",                            [0, 0, 0, 0],                 0)
check("strictly increasing heights",          [1, 2, 3, 4, 5, 6, 7, 8, 9],  20)
check("strictly decreasing heights",          [9, 8, 7, 6, 5, 4, 3, 2, 1],  20)
check("v-shape heights",                      [10, 1, 1, 1, 10],            40)
check("large values",                         [10000, 10000],               10000)
check("tall lines close vs short lines wide", [1, 100, 100, 1],             100)

# mutation check
orig = [1, 8, 6, 2, 5, 4, 8, 3, 7]
orig_copy = orig.copy()
res = max_area(orig)
part1_total += 1
if orig != orig_copy:
    part1_fail += 1
    print("FAIL [does not mutate original list]")
    print(f"  original list was modified: changed from {orig_copy!r} to {orig!r}\n")

print(f"Part 1 (Correctness): {part1_total - part1_fail}/{part1_total} passed")


# ── Part 2: Algorithmic Efficiency ────────────────────────────────────────────

if part1_fail > 0:
    print("\nPart 2 (Algorithmic Efficiency): skipped (fix Part 1 correctness first)")
else:
    print("\nPart 2 (Algorithmic Efficiency):")

    # 1. Time complexity check: 30k items must complete in < 1.0s
    part2_total += 1
    large_list = list(range(1, 30001))
    start_time = time.perf_counter()
    ans_time = max_area(large_list)
    elapsed = time.perf_counter() - start_time

    expected_large = 225000000
    if ans_time != expected_large:
        part2_fail += 1
        print("FAIL [time: large list correctness]")
        print(f"  expected: {expected_large}, got: {ans_time!r}\n")
    elif elapsed > 1.0:
        part2_fail += 1
        print("FAIL [time: O(n) requirement]")
        print(f"  took: {elapsed:.2f}s (must finish in < 1.0s; avoid O(n^2) nested loops)\n")
    else:
        print(f"  [PASS] time complexity: {elapsed:.3f}s (< 1.0s, O(n) verified)")

    # 2. Space complexity check: must use O(1) auxiliary space (< 50 KB peak allocation)
    if part2_fail > 0:
        print("  [SKIP] space complexity check skipped (fix time complexity first)")
    else:
        part2_total += 1
        stress_data = list(range(1, 50001))

        tracemalloc.start()
        ans_space = max_area(stress_data)
        _, peak_bytes = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_kb = peak_bytes / 1024
        if ans_space != 625000000:
            part2_fail += 1
            print("FAIL [space: stress test correctness]")
            print(f"  expected: 625000000, got: {ans_space!r}\n")
        elif peak_bytes > 50 * 1024:
            part2_fail += 1
            print("FAIL [space: O(1) auxiliary space requirement]")
            print(f"  peak memory allocated: {peak_kb:.1f} KB (limit: 50.0 KB)")
            print("  Auxiliary memory allocation detected. Refactor to O(1) space!\n")
        else:
            print(f"  [PASS] space complexity: {peak_kb:.1f} KB (< 50.0 KB, O(1) auxiliary space verified)")

    print(f"\nPart 2 result: {part2_total - part2_fail}/{part2_total} passed")

    if part2_fail == 0:
        print("\nBIM!!!")
    else:
        print("\nDrill incomplete: Part 2 efficiency requirements must pass to finish this drill.")
