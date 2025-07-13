from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        counter = Counter(text)
        haha = 'balloon'
        status = True
        while status:
            for letter in haha:
                if letter not in counter:
                    status = False
                    break
                elif counter[letter] == 1:
                    del counter[letter]
                else:
                    counter[letter] -= 1
            if status:
                count +=1
        return count