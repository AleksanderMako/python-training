class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0
        palindorme_len = -1
        for i in range(len(s)):
            palindorme_len = max(self.pali(s, i, i+1), self.pali(s, i, i))

            if palindorme_len > end - start:
                start = i - int((palindorme_len-1)/2)
                end = i+int(palindorme_len/2)
        return s[start:end+1]

    def pali(self, s: str, l: int, r: int) -> int:

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r-l-1
