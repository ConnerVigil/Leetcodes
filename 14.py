class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        base = strs[0] # Use first word

        for i in range(len(base)):
            for word in strs[1:]:
                # Loop through the rest of words and check the word at i
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]

        return base

    # Write a function to find the longest common prefix string amongst an array of strings.
    #
    # If there is no common prefix, return an empty string "".
    #
    #
    # Example 1:
    #
    # Input: strs = ["flower","flow","flight"]
    # Output: "fl"
    # Example 2:
    #
    # Input: strs = ["dog","racecar","car"]
    # Output: ""
    # Explanation: There is no common prefix among the input strings.