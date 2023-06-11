//Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

//We need to check for all the negative elements which are in non increasing order so we know that once we come accross a negative number the rest numbers in that column and row would be negative.

//Firstly we will check if the first number of matrix i.e grid[0][0] is negative or not.
//if it is then the entire grid has negative numbers only.
//if not then we can traverse matrix element by element and as soon as a negative number is encountered add the remaining elemens of row to answer and move to next row.

class Solution {
    public int countNegatives(int[][] grid) {
        int ans = 0;
        if(grid[0][0] < 0){
            return (grid.length)*(grid[0].length);
        }else{
            for(int i = 0 ; i < grid.length ; i++){
                for(int j = 0 ; j < grid[0].length ; j++){
                    if(grid[i][j] < 0){
                        ans += grid[0].length - j;
                        break;
                    }
                }
            }
        }
        return ans;
    }
}
