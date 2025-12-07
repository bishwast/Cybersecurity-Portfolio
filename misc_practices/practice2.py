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

#     """
#     Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#     Example 1:
#     Input: s = "anagram", t = "nagaram"
#     Output: true
#     """
#     def isAnagram(self, s: str, t: str) -> bool:
#         """
#         1. Add one token for every character in s.
#         2. Remove one token for every character in t.
#         3. If you ever try to remove a token that doesn’t exist → t is not an anagram.
#         4. If all tokens are removed perfectly → they are anagrams.
#         """
#         # Validate false if not anagram: Exit
#         if len(s) != len(t):
#             return False
#
#         count = {} # Dictionary to store count of characters in string
#         # Setup the count
#         for c in s:
#             if c in count:      # If c is in the dictionary count
#                 count[c] += 1   # Increment the count by 1
#             else:
#                 count[c] = 1    # Else, set the count as 1
#         for c in t:
#             if c in count:
#                 count[c] -=1
#                 if count[c] < 0:        # That means if count negative, characters in t is more than s
#                     return False        # Not anagram
#             else:                       # Else, if character is not in t: not anagram
#                 return False
#         #else, its true
#         return True
# s3 = Solution()
# s = "anagram"
# t = "nagaram"
# result = s3.isAnagram(s,t)
# print(f"Is \"{s}\" anagram with \"{t}\": {result}")

#     """
#     Given an integer array nums, return true if any value appears at least twice in the array,
#     and return false if every element is distinct.
#     Example 1:
#     Input: nums = [1,2,3,1]
#     Output: true
#     Explanation:
#     The element 1 occurs at the indices 0 and 3.
#     """
#
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         """
#         Contains Duplicate Problem
#         parameter: List of number
#         return: bool - T/F
#         """
#         seen = set()    # set() eliminates duplicate
#         for n in nums:
#             if n in seen:
#                 return True
#             else:
#                 seen.add(n)
#         return seen
# s4 = Solution()
# nums = [1, 2, 3, 1]
# contains_duplicate = s4.containsDuplicate(nums)
# print(f"Do {nums} contains duplicate: {contains_duplicate}")

#     """
#     Given an array of integers nums and an integer target,
#     return indices of the two numbers such that they add up to target.
#     return number related to respective indices that add up to target.
#     You may assume that each input would have exactly one solution, and you may not use the same element twice.
#     You can return the answer in any order.
#     Example 1:
#     Input: nums = [2,7,11,15], target = 9
#     Output: [0,1] and 2,7
#     Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#     """
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}                               # Store indices. Maps number to index
#
#         for i, num in enumerate(nums):                              # Loop through nums, i = index, num = value
#             complement = target - num                               # Complement to meet the target
#             if complement in seen:                                  # If we already saw the number needed to reach target
#                 return [seen[complement], i  ], [complement, num]   # Index and Numbers of the previously seen complement and current index form the solution
#             else:
#                 seen[num] = i                                       # Store num with its index for future complement lookup
#         return [], []
# s5 = Solution()
# nums = [2,7,11,15]
# target = 9
# two_sum = s5.twoSum(nums, target)
# indices, numbers = two_sum
# print(f"Two Sum Results from List {nums}: \ntarget: {target}\nindices: {indices}\nnumbers: {numbers} ")

#     """
#     Given an array nums of size n, return the majority element.
#     The majority element is the element that appears more than ⌊n / 2⌋ times.
#     You may assume that the majority element always exists in the array.
#     Input: nums = [2,2,1,1,1,2,2]
#     Output: 2
#     """
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate = None                # Candidate = Current number considered as the majority element
#         count = 0                       # Counter for tracking the current candidate
#
#         for n in nums:                  # Loop/Iterate through each number in list of nums
#             if count == 0:              # If the counter is 0, pick the number as a new candidate
#                 candidate = n
#             if n == candidate:          # If current number-n, matches new candidate, increment the counter
#                 count +=1
#             else:                       # Else, decrement counter
#                 count -=1
#         return candidate                # Majority Element
# s6 = Solution()
# nums = [2,2,1,1,1,2,2]
# mj_element = s6.majorityElement(nums)
# print(f"Majority Elements: {mj_element}")

#     """
#     You are given an m x n integer grid accounts
#     where accounts[i][j] is the amount of money the i-th customer has in the j-th bank.
#     Return the wealth that the richest customer has.
#     A customer's wealth is the amount of money they have in all their bank accounts.
#     The richest customer is the customer that has the maximum wealth.
#     """
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         max_wealth = 0
#         for customer in accounts:
#             customer_wealth = 0
#             for amount in customer:
#                 customer_wealth += amount
#             if customer_wealth > max_wealth:
#                 max_wealth = customer_wealth
#         return max_wealth
# s7 = Solution()
# accounts = [[1,2,3],[3,2,1]]
# max_wealth = s7.maximumWealth(accounts)
# print(f"Max Wealth: {max_wealth}")

# Matrix Diagonal
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         """
#         Given a square matrix mat, return the sum of the matrix diagonals.
#         Only include the sum of all the elements on the primary diagonal
#         and all the elements on the secondary diagonal that are not part of the primary diagonal.
#
#         Example:
#         Input:
#         mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
#         Output: 8
#         :param mat:
#         :return: sum of the matrix diagonals
#         """
#
#         n = len(mat)
#         total_sum = 0
#
#         for i in range(n):
#             # primary diagonal
#             total_sum += mat[i][i]
#             # secondary diagonal
#             total_sum += mat[i][n-1-i]
#
#             # If n is odd, subtract central common index numbers once
#             if n % 2 == 1 and i == n // 2:
#                 total_sum -= mat[i][i]
#         return total_sum
#
# mat = [[1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1]]
# s8 = Solution()
# t_sum = s8.diagonalSum(mat)
# print(f"The sum of the matrix diagonals;  \n\tMatrix {mat} : Diagonals Sum {t_sum}")

# # Flipping an Image
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         """
#         Given an n x n binary matrix image, flip the image horizontally, then invert it,
#         and return the resulting image.
#
#         To flip an image horizontally means that each row of the image is reversed.
#         For example, flipping [1,1,0] horizontally results in [0,1,1].
#
#         To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#         For example, inverting [0,1,1] results in [1,0,0].
#
#         Example:
#         Input: image = [[1,1,0],[1,0,1],[0,0,0]]
#         Output: [[1,0,0],[0,1,0],[1,1,1]]
#
#         Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
#         Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
#
#         :param image:
#         :return: the resulting flipped image
#         """
#         n = len(image)
#
#         for i in range(n):
#             image[i].reverse()     # Flip Image Horizontally : flipping [1,1,0] horizontally results in [0,1,1]
#
#             for j in range(n):      # Invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0
#                 """
#                 If image[i][j] = 1 → 1 - 1 = 0
#
#                 If image[i][j] = 0 → 1 - 0 = 1
#                 """
#                 image[i][j] = 1 - image[i][j]
#         return image
#
# s9 = Solution()
# image = [[1,1,0],[1,0,1],[0,0,0]]
# f_i_img = s9.flipAndInvertImage(image)
# print(f"Flipped {image} to \n\t\t\t{f_i_img}")











