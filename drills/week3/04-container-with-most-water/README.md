# Container With Most Water

## Problem
You are given a list of non-negative integers `height` where each number represents the height of a vertical line at that index.

Choose two lines that, together with the x-axis, form a container that stores the maximum amount of water.

Return the maximum area of water the container can hold.

The distance between two lines is the difference between their indices (`right - left`). The container's height is determined by the shorter of the two lines (`min(height[left], height[right])`). The lines cannot be slanted.

## Function Signature
`max_area(height) -> int`

## Examples
| input | output | why |
|---|---|---|
| `[1, 8, 6, 2, 5, 4, 8, 3, 7]` | `49` | lines at index 1 (height 8) and index 8 (height 7) give width 7, height 7: area = 49 |
| `[1, 1]` | `1` | only two lines: width 1, height 1: area = 1 |
| `[1, 2, 1]` | `2` | lines at index 0 and 2 give width 2, height 1: area = 2 |
| `[4, 3, 2, 1, 4]` | `16` | lines at index 0 and 4 give width 4, height 4: area = 16 |
| `[1, 2, 4, 3]` | `4` | lines at index 1 and 3 give width 2, height 2: area = 4 |
| `[5, 5, 5, 5]` | `15` | widest boundaries give width 3, height 5: area = 15 |
| `[2, 3, 10, 5, 7, 8, 9]` | `36` | lines at index 2 (height 10) and index 6 (height 9) give width 4, height 9: area = 36 |
| `[0, 2]` | `0` | shorter line is 0, so no water can be held |
| `[5]` | `0` | fewer than two lines cannot form a container |
| `[]` | `0` | empty list forms no container |

## Requirements
To complete this drill, your solution must pass both parts:
1. **Part 1 — Correctness**: return the maximum possible water area for all test cases without modifying the input list.
2. **Part 2 — Algorithmic Efficiency**:
   - **Time complexity:** $O(n)$ time. A brute-force nested loop ($O(n^2)$) comparing every pair will time out on large inputs.
   - **Space complexity:** $O(1)$ auxiliary space. Do not create auxiliary lists or copies.

## Assumptions
- `height` contains non-negative integers (heights $\ge 0$)
- fewer than two lines (`len(height) < 2`) cannot form a container; return `0`
- container walls must be perpendicular to the x-axis (no slanting)
- do not modify the original list

## Hint
Start by writing a brute-force solution with two nested loops to verify the calculation and get Part 1 to pass.

To achieve $O(n)$ time for Part 2, consider the **two-pointer technique**:
- What happens if you start with pointers at the extreme ends (widest possible width)?
- As you narrow the distance between pointers, the width always decreases.
- Which pointer should you move inward to have any chance of finding a larger area: the one pointing to the shorter line, or the taller line? Why?
