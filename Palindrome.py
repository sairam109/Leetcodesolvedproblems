//palindrome number- https://leetcode.com/problems/palindrome-number/
//runtime-52ms, memory-14.5mb
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x==x[::-1]:
            return 1
        else:
            return 0
