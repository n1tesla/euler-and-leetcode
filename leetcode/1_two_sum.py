from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_i = 0
        index_j = 0
        for i in nums:

            for j in nums:

                if (i+j==target) and (index_j!=index_i):
                    return [index_i,index_j]
                else:
                    index_j+=1
            index_j=0
            index_i+=1




nums=[2,7,11,15]
nums2=[3,2,4]
nums3=[3,3]


sol=Solution()
print(sol.twoSum(nums,target=9))
print(sol.twoSum(nums2,target=6))
print(sol.twoSum(nums3,target=6))


