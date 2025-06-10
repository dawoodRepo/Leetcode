from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictionary = defaultdict(list)
        for word in strs:
            a=[0] * 26
            for letter in word:
                a[ord(letter) - ord('a')] += 1
            a = tuple(a)
            dictionary[a].append(word)
            
        return list(dictionary.values())

        # my approach
        # counter = {}
        # for word in strs:
        #     count=[0] * 26
        #     for letter in word:
        #         temp = ord(letter) - ord('a')
        #         count[temp] += 1
        #     count = tuple(count)
        #     if count in counter:
        #         counter[count].append(word)
        #     else:
        #         counter[count] = [word]

        # return list(counter.values())