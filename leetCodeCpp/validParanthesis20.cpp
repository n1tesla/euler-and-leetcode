#include <iostream>
#include <stack>
using namespace std;
bool isValid(std::string s)
{
	stack<char> st;
	for (int i = 0; i < s.size(); ++i)
	{
		char bracket = s[i];
		if (bracket == '(' || bracket == '{' || bracket == '[') {
			st.push(bracket);
		}
		else
		{
			// Must check if stack is empty before calling .top()
			if (st.empty()) return false;

			char top = st.top();
			if ((top == '(' && bracket == ')') ||
				(top == '{' && bracket == '}') ||
				(top == '[' && bracket == ']'))
			{
				st.pop();
			}
			else
				return false;
		}
	}
	// If the stack is empty, all brackets were matched correctly
	return st.empty();
}


int main()
{
	std::string s = "([{])";
	bool validParenthesis = isValid(s);
	// Using boolalpha prints "true/false" instead of "1/0"
	cout << boolalpha << validParenthesis << endl;

	return 0;

}