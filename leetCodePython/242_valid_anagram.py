class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted=''.join(sorted(s))
        t_sorted=''.join(sorted(t))
        if s_sorted==t_sorted:
            return True
        else:
            return False

sol=Solution()
test_anagram=[["anagram","nagaram"],["rat","car"]]
for i in test_anagram:
    print(sol.isAnagram(i[0],i[1]))
