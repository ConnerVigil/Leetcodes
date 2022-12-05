class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        longest = s[0]
        hashset = set()
        left = 0
        right = 0

        while right < len(s):

            if s[right] not in hashset:
                hashset.add(s[right])
                right += 1

                if right - left > len(longest):
                    longest = s[left:right]

            else:
                hashset.remove(s[left])
                left += 1

        return len(longest)


# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
