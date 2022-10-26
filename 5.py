def longestPalindrome(s):
    resWord = ""
    resLength = 0

    for i in range(len(s)):  # Iterate through characters in string

        # odd length words
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:  # While pointers in range and two chars are equal
            if right - left + 1 > resLength:
                resWord = s[left:right + 1]
                resLength = right - left + 1
            left -= 1
            right += 1

        # even length words
        left, right = i, i + 1  # Offset to account for even length palindromes
        while left >= 0 and right < len(s) and s[left] == s[right]:  # While pointers in range and two chars are equal
            if right - left + 1 > resLength:
                resWord = s[left:right + 1]
                resLength = right - left + 1
            left -= 1
            right += 1

    return resWord


print(longestPalindrome("babad"))

# Given a string s, return the longest palindromic substring in s.
#
# A string is called a palindrome string if the reverse of that string is the same as the original string.
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
