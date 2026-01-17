#include <iostream>
#include <vector>
#include <cmath>


std::vector<int> plusOne(std::vector<int>& digits) {
	for (int i = digits.size() - 1; i >= 0; --i) {
		if (digits[i] < 9) {
			digits[i]++;
			return digits;
		}
		digits[i] = 0;
	}
	digits.insert(digits.begin(), 1);
	return digits;
}


int main()
{
	//std::vector<int> vec = { 1,3,9 };
	//plusOne(vec);
	std::vector<int> vec = { 1,3,9 };
	std::vector<int> result = plusOne(vec);

	std::cout << "Input: [1, 2, 3] → Output: [";
	for (int i = 0; i < result.size(); ++i) {
		std::cout << result[i];
		if (i < result.size() - 1) std::cout << ", ";
	}
	std::cout << "]" << std::endl;

	return 0;
}