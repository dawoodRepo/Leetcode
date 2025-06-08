from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # approach 1
        if len(s) != len(t): return False   #edge case
        
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict


        # approach 2
        # counter = {}
        # for l in s:
        #     if l in counter:
        #         counter[l] +=1
        #     else:
        #         counter[l] = 1

        # for l in t:
        #     if l not in counter:
        #         return False
        #     elif counter[l] == 1:
        #         del counter[l]
        #     else:
        #         counter[l] -=1

        # return True