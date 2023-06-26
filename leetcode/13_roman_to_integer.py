class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}

        total_count=0
        list_s=list(reversed(s))
        for k,v in enumerate(reversed(s)):

            if k==0:
                total_count+=roman_dict[v]
                continue
            if roman_dict[v]>=roman_dict[list_s[k-1]]:
                total_count+=roman_dict[v]
            else:
                total_count-=roman_dict[v]

        return total_count