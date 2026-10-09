# Minimum Insertions to Balance a Parentheses String

Solution to LeetCode 1541.

## Problem

Given a string `s` containing only `'('` and `')'`, return the minimum number of insertions needed to make it balanced.

A string is balanced if:

- Every `'('` has a corresponding two consecutive `'))'`.
- Each `'('` comes before its corresponding `'))'`.

You may insert `'('` or `')'` at any position.

### Examples

| Input | Output | Explanation |
|---|---|---|
| `"(()))"` | 1 | Add one `)` at the end to get `"(())))"` |
| `"())"` | 0 | Already balanced |
| `"))())("` | 3 | Add `(` at the start, and `))` at the end |

### Constraints

- `1 <= s.length <= 10^5`
- `s` consists only of `'('` and `')'`

## Approach

A greedy single pass over the string, tracking:

- `opened`: the number of unmatched `'('` so far
- `half`: whether a single `')'` has been seen and is waiting for its pair
- `ans`: the number of insertions made so far

For each character:

- **`'('`**: If a lone `')'` is waiting (`half`), insert one `')'` to complete the pair and match it to an open `'('` (or insert a `'('` if none is open). Then count the new `'('` in `opened`.
- **`')'`**: If a `')'` is already waiting, the two form a `'))'` pair and match one open `'('` (or insert a `'('` if none is open). Otherwise, mark `half = True`.

At the end, a lone waiting `')'` is completed with one insertion, and each remaining open `'('` needs `'))'`, so the answer is `ans + 2 * opened`.

## Solution

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        opened = 0       # unmatched '(' so far
        half = False     # saw one ')' and waiting for its pair

        for c in s:
            if c == '(':
                if half:
                    ans += 1          # add ')' to complete the pair
                    half = False
                    if opened:
                        opened -= 1
                    else:
                        ans += 1      # no '(' to match, add one
                opened += 1
            elif half:
                half = False
                if opened:
                    opened -= 1
                else:
                    ans += 1
            else:
                half = True

        if half:
            ans += 1
            if opened:
                opened -= 1
            else:
                ans += 1

        return ans + 2 * opened
```

## Complexity

- **Time:** O(n), a single pass over the string
- **Space:** O(1)

## Usage

```python
sol = Solution()
print(sol.minInsertions("(()))"))   # 1
print(sol.minInsertions("())"))     # 0
print(sol.minInsertions("))())("))  # 3
```
