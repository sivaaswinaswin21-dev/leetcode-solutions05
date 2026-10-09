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