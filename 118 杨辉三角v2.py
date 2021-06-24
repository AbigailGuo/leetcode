class Solution:
    def generate(self, numRows: int):
        def yh(numRows):
            result = [[1], [1, 1]]
            n = 2
            while n<numRows:
                yield result
                L = result[len(result)-1][:]
                for i in range(1, len(L)):
                    L[i] =  result[len(result)-1][i-1]+result[len(result)-1][i]
                L.append(1)
                result.append(L)
                n += 1
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            yh_array = []
            for array in yh(numRows):
                yh_array = array
            return yh_array


s = Solution()
print(s.generate(2))