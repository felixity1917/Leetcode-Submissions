class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=''
        for i in range(len(str(x))-1,-1,-1):
            i1=str(x)[i]
            a+=i1
        if a==str(x):
            return True
        else:
            return False
