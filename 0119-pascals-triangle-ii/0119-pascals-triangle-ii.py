class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1] * (i + 1) for i in range(rowIndex+1)]

        for i in range(2, rowIndex+1):
            for j in range(1, len(result[i])-1):
                result[i][j] = result[i-1][j-1] + result[i-1][j]

        return result[rowIndex]
        # return result[rowIndex-1]