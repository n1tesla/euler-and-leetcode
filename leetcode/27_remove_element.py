from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        indicies = []
        for key, value in enumerate(nums):
            if val == value:
                indicies.append(key)
                k += 1
        len_nums=len(nums)
        for i in sorted(indicies, reverse=True):
            del nums[i]

        return len_nums-k

val=2
nums=[0,1,2,2,3,0,4,2]
nums2=[3,2,2,3]
sol=Solution()
print(sol.removeElement(nums,val))