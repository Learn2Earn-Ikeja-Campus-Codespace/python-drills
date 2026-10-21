# 3Sum

## Problem
Given a list of integers `numbers`, find all unique triplets `[numbers[i], numbers[j], numbers[k]]` such that:
1. The three indices `i`, `j`, and `k` are distinct (`i != j`, `i != k`, `j != k`).
2. The sum of the three elements equals zero (`numbers[i] + numbers[j] + numbers[k] == 0`).
3. The solution must not contain duplicate triplets.

The order of triplets in the output and the order of elements within each triplet does not matter.

## Function Signature
`three_sum(numbers) -> list[list[int]]`

## Examples
| input | output | why |
|---|---|---|
| `[-1, 0, 1, 2, -1, -4]` | `[[-1, -1, 2], [-1, 0, 1]]` | `-1 + -1 + 2 = 0` and `-1 + 0 + 1 = 0` |
| `[0, 0, 0]` | `[[0, 0, 0]]` | only one valid triplet summing to zero |
| `[0, 0, 0, 0]` | `[[0, 0, 0]]` | duplicate combinations must be excluded |
| `[1, 2, -2, -1]` | `[]` | no three numbers sum to zero |
| `[-2, 0, 1, 1, 2]` | `[[-2, 0, 2], [-2, 1, 1]]` | two distinct valid triplets |
| `[-1, -1, -1, 2, 2]` | `[[-1, -1, 2]]` | duplicates skipped |
| `[3, -2, 1, 0]` | `[]` | no valid triplet sums to 0 |
| `[-4, -1, -1, 0, 1, 2]` | `[[-1, -1, 2], [-1, 0, 1]]` | only one 2 is available, so `[-4, 2, 2]` cannot be formed |
| `[0]` | `[]` | fewer than 3 elements |
| `[]` | `[]` | empty list |

## Requirements
To complete this drill, your solution must pass both parts:
1. **Part 1 — Correctness**: return all unique triplets that sum to zero without duplicates. Do not modify the original list.
2. **Part 2 — Algorithmic Efficiency**:
   - **Time complexity:** $O(n^2)$ time. A brute-force solution with three nested loops ($O(n^3)$) will time out.
   - **Space complexity:** $O(1)$ auxiliary space (excluding the output list and space used by sorting).

## Assumptions
- `numbers` contains integers (positive, negative, or zero)
- if fewer than three numbers are provided, return `[]`
- each index can only be used once per triplet
- no duplicate triplets in the returned list
- do not modify the original list

## Hint
A brute-force solution checks every triplet using 3 nested loops ($O(n^3)$), which is too slow.

To achieve $O(n^2)$:
- What if you sort the array first?
- Once sorted, if you fix the first number `numbers[i]`, how can you use two pointers (left and right) to find the remaining two numbers in $O(n)$ time?
- How can you skip identical adjacent values to avoid generating duplicate triplets without needing an extra set?
