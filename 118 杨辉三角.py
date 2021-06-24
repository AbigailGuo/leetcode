class Solution:
    def generate(self, numRows: int):
        result = []
        if numRows == 1:
            result = [1]
        elif numRows == 2:
            result = [1, 1]
        elif numRows>2:
            result = [[1], [1,1]]
            for i in range(2, numRows):
                L = result[len(result)-1][:]
                for j in range(1, len(result[len(result)-1])):
                    L[j]= result[len(result)-1][j-1]+ result[len(result)-1][j]
                L.append(1)
                result.append(L)
        return (result)

s = Solution()
print(s.generate(5))
        



