#include <iostream>
#include <vector>

using namespace std;


int searchInsert(vector<int>& nums, int target)
{
	for (int i = 0; i < nums.size(); ++i)
	{
		
		if (nums[i] < target)
			continue;
		if (target == nums[i])
			return i;
		if (target > nums[i - 1] && nums[i] > target)
			return i;

	}
	return nums.size();
}



//int main()
//{
//	vector<int> nums = { 1,3,4,5,6 };
//	int target = 8;
//
//	std::cout<<searchInsert(nums, target);
//}