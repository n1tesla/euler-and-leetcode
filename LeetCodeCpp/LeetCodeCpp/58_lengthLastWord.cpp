#include <iostream>

int lengthOfTheLastWord(std::string s)
{
	std::string lastWord;
	bool isObserveFirstLetter = false;
 	for (int i = s.size()-1 ; i>=0; --i)
	{
		if (s[i] == ' ' && isObserveFirstLetter)
			return lastWord.size();
		else if (s[i] != ' ') {
			isObserveFirstLetter = true;
			lastWord += s[i];
		}
		
	}
	return lastWord.size();

}

//int main()
//{
//	std::string s = "Hello World";
//	//std::string s = "   fly me   to   the moon  ";
//	//std::string s = "Tunahan ";
//	std::cout<<lengthOfTheLastWord(s);
//
//}


