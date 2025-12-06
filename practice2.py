from typing import List, Dict
class Solution:
    # """
    # Write a function that reverses a string. The input string is given as an array of characters s.
    # You must do this by modifying the input array in-place with O(1) extra memory.
    # Example 1:
    #
    # Input: s = ["h","e","l","l","o"]
    # Output: ["o","l","l","e","h"]
    # """
    #
    # def reverseString(self, s: List[str]) -> None:
    #     s[:]=s[::-1]

# s=Solution()
# sl = ["h","e","l","l","o"]
# s.reverseString(sl)
# print(sl)

#     """
#     Given a valid (IPv4) IP address, return a defanged version of that IP address.
#     A defanged IP address replaces every period "." with "[.]".
#     Example 1:
#     Input: address = "1.1.1.1"
#     Output: "1[.]1[.]1[.]
#     """
#
#     def defangIPaddr(self, address: str) -> str:
#         defangedIps = []
#         for symbol in address:
#             if symbol == ".":
#                 defangedIps.append("[.]")
#             else:
#                 defangedIps.append(symbol)
#         return "".join(defangedIps)     # Join list into the string
# s2 = Solution()
# address = "1.1.1.1"
# dfs = s2.defangIPaddr(address)
# print(dfs)  # 1[.]1[.]1[.]1

    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. Add one token for every character in s.
        2. Remove one token for every character in t.
        3. If you ever try to remove a token that doesn’t exist → t is not an anagram.
        4. If all tokens are removed perfectly → they are anagrams.
        """
        # Validate false if not anagram: Exit
        if len(s) != len(t):
            return False

        count = {} # Dictionary to store count of characters in string
        # Setup the count
        for c in s:
            if c in count:      # If c is in the dictionary count
                count[c] += 1   # Increment the count by 1
            else:
                count[c] = 1    # Else, set the count as 1
        for c in t:
            if c in count:
                count[c] -=1
                if count[c] < 0:        # That means if count negative, characters in t is more than s
                    return False        # Not anagram
            else:                       # Else, if character is not in t: not anagram
                return False
        #else, its true
        return True
s3 = Solution()
s = "anagram"
t = "nagaram"
result = s3.isAnagram(s,t)
print(f"Is \"{s}\" anagram with \"{t}\": {result}")



