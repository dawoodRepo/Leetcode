class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # step .1
        # count no of occurences of each letter in magazine and store in hashmap(dict)
        counter = {}
        for l in magazine:
            if l in counter:
                counter[l] +=1
            else:
                counter[l] = 1
        # step .2
        for l in ransomNote:
            if l not in counter:
                return False
            elif counter[l] == 1:
                del counter[l]
            elif l in counter:
                counter[l] -=1
            
        return True