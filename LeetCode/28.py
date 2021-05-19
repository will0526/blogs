from typing import List


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        m = len(haystack)
        n = len(needle)

        if n == 0: return 0

        nextArr = [0]

        i = 1
        j = 0
        for i in range(1,n-1):
            while j>0 and needle[i]!=needle[j]:
                j = nextArr[j-1]
            if needle[i]==needle[j]:
                j+=1

            nextArr.insert(i, j)

        i = 0
        j = 0


        while i < m:

            while j>0 and haystack[i] != needle[j]:
                j = nextArr[j-1]

            if haystack[i] == needle[j]:
                j+=1

            if j == n:
                return i-n+1
            i+=1

        return -1

s = Solution()

print(s.strStr("hell0","ll"))