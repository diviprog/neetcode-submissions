class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            row = (r+l)//2
            if target < matrix[row][0]:
                r = row-1
            elif target > matrix[row][-1]:
                l = row+1
            else:
                break
        else:
            return False
        
        l, r = 0, len(matrix[row])-1
        while l <= r:
            m = (r+l)//2
            if target == matrix[row][m]:
                return True
            elif target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
        return False