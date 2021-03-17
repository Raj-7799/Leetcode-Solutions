class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int columns = matrix[0].size();
        int low = 0;
        int high = (rows * columns) - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int row = mid / columns;
            int column = (mid) % columns;
            
            if (matrix[row][column] == target) {
                return true;
            } else if (matrix[row][column] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return false;
    }
};
