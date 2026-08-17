class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        freq = {}
        maxlen = 0
        for r in range(len(s)):
            char = s[r]
            if char in freq and freq[char]>=l:
                l=freq[char]+1
            freq[char]=r
            maxlen = max(maxlen, r-l+1)
        return maxlen