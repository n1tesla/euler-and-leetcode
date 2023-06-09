from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            sub_list=nums[nums.index(i)+1:]
            for j in sub_list:
                sum=i+j
                if sum==target:
                    return [nums.index(i),sub_list.index(j)+1]



nums=[2,7,11,15]
nums2=[3,2,6,4]
nums3=[3,3]


sol=Solution()
#print(sol.twoSum(nums,target=9))
print(sol.twoSum(nums2,target=6))
print(sol.twoSum(nums3,target=6))


