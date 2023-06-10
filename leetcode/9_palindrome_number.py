class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        string_x=str(x)
        for k,v in enumerate(string_x):
            if k>len(string_x)/2:
                break
            index=len(string_x)-k-1
            if v!=string_x[index]:
                return False
        return True

test_x=[121,10,11111,1000,1221,-500]
sol=Solution()

for x in test_x:
    print(sol.isPalindrome(x))