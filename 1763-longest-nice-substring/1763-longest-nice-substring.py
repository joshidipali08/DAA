class Solution:
    def longestNiceSubstring(self, s):
        ans = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]

                if all(c.lower() in sub and c.upper() in sub for c in sub):
                    if len(sub) > len(ans):
                        ans = sub

        return ans