class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
        # right
            for j in range(len(matrix[0])):
                ans.append(matrix[0].pop(0))
                if not matrix[0]:
                    matrix.pop(0)
            # down
            j=0
            while j < len(matrix):
                if matrix[j]:
                    ans.append(matrix[j].pop(-1))
                if not matrix[j]:
                    matrix.pop(j)
                else:
                    j+=1
            # left
            if matrix:
                for j in range(len(matrix[-1])):
                    ans.append(matrix[-1].pop(-1))
                    if not matrix[-1]:
                        matrix.pop(-1)
            # up
            if matrix:
                for j in reversed(range(len(matrix))):
                    if matrix[j]:
                        ans.append(matrix[j].pop(0))
            
        return ans