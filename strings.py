# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time complexity : O(2n) = O(n)O(2n)=O(n).
# In the worst case each character will be visited twice by ii and jj.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        result = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            result = max(result, right - left + 1)

            right += 1
        return result