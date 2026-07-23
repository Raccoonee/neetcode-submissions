class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, h_row = 0, len(matrix) - 1
        l_column, h_column = 0, len(matrix[0]) - 1

        
        while l_row <= h_row:
            mid_row = (l_row + h_row) // 2
    
            if matrix[mid_row][-1] < target:
                l_row = mid_row + 1    
            elif matrix[mid_row][0] > target:
                h_row = mid_row - 1
            else:    
                while l_column <= h_column:
                    mid_column = (l_column + h_column) // 2
                    if matrix[mid_row][mid_column] == target:
                            return True
                    if matrix[mid_row][mid_column] < target:
                            l_column = mid_column + 1
                    if matrix[mid_row][mid_column] > target:
                            h_column = mid_column - 1 
                return False      
                        
        return False