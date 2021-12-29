//coins arrange-https://leetcode.com/problems/arranging-coins/submissions/
  // runtime- 1703ms memory-13.9mb
  class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=0
        c=1
        while n>=c:
            n-=c
            c=c+1
            l=l+1
        return l
