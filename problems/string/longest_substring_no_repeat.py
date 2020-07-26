class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 1:
            return 0
        if len(s) == 1:
            return 1
        j = 0
        max_len = -1
        seen = {}
        i = 0
        while j < len(s) and i < len(s):
            if s[i] not in seen:
                seen[s[i]] = True
                i += 1
            else:
                max_len = max(max_len, i-j)
                seen = {}
                j += 1
                i = j

        return max(max_len,i-j)
