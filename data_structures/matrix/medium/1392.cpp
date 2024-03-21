// Check if There is a Valid Path in a Grid
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        int p1=0, p2=0;
        vector<vector<int>>v(grid.size(), vector<int>(grid[0].size(), 0));
        vector<vector<int>>v1(grid.size(), vector<int>(grid[0].size(), 1));
        queue<pair<int, int>>q;
        v[0][0]=1;
        q.push({0, 0});
        
        while(!q.empty()){
            int x=q.front().first, y=q.front().second;
            p1=x; p2=y;
            q.pop();
            if(x==grid.size()-1 && y==grid[0].size()-1){return true;}
            if(grid[x][y]==1){
                if(y<grid[0].size()-1 && !v[x][y+1] && (grid[x][y+1]==3 || grid[x][y+1]==5 || grid[x][y+1]==1)){
                    v[x][y+1]=1;
                    q.push({x, y+1});
                }
                if(y>0 && !v[x][y-1] && (grid[x][y-1]==4 || grid[x][y-1]==6 || grid[x][y-1]==1)){
                    v[x][y-1]=1;
                    q.push({x, y-1});
                }
            }
            else if(grid[x][y]==2){
                if(x<grid.size()-1 && !v[x+1][y] && (grid[x+1][y]==5 || grid[x+1][y]==6 || grid[x+1][y]==2)){
                    v[x+1][y]=1;
                    q.push({x+1, y});
                }
                if(x>0 && !v[x-1][y] && (grid[x-1][y]==4 || grid[x-1][y]==3 || grid[x-1][y]==2)){
                    q.push({x-1, y});
                    v[x-1][y]=1;
                }
            }
            else if(grid[x][y]==3){
                if(x<grid.size()-1 && !v[x+1][y] && (grid[x+1][y]==5 || grid[x+1][y]==6 || grid[x+1][y]==2)){
                    v[x+1][y]=1;
                    q.push({x+1, y});
                }
                if(y>0 && !v[x][y-1] && (grid[x][y-1]==4 || grid[x][y-1]==6 || grid[x][y-1]==1)){
                    q.push({x, y-1});
                    v[x][y-1]=1;
                }
            }
            else if(grid[x][y]==4){
                if(x<grid.size()-1 && !v[x+1][y] && (grid[x+1][y]==5 || grid[x+1][y]==6 || grid[x+1][y]==2)){
                    v[x+1][y]=1;
                    q.push({x+1, y});
                }
                if(y<grid[0].size()-1 && !v[x][y+1] && (grid[x][y+1]==1 || grid[x][y+1]==3) || grid[x][y+1]==5){
                    q.push({x, y+1});
                    v[x][y+1]=1;
                }
            }
            else if(grid[x][y]==5){
                if(x>0 && !v[x-1][y] && (grid[x-1][y]==2 || grid[x-1][y]==3 || grid[x-1][y]==4)){
                    v[x-1][y]=1;
                    q.push({x-1, y});
                }
                if(y>0 && !v[x][y-1] && (grid[x][y-1]==1 || grid[x][y-1]==4 || grid[x][y-1]==3)){
                    q.push({x, y-1});
                    v[x][y-1]=1;
                }
            }
            else if(grid[x][y]==6){
                if(x>0 && !v[x-1][y] && (grid[x-1][y]==1 || grid[x-1][y]==3 || grid[x-1][y]==5)){
                    v[x-1][y]=1;
                    q.push({x-1, y});
                }
                if(y<grid[0].size()-1 && !v[x][y+1] && (grid[x][y+1]==1 || grid[x][y+1]==3 || grid[x][y+1]==5)){
                    q.push({x, y+1});
                    v[x][y+1]=1;
                }
            }
        }
        if(p1!=grid.size()-1 && p2!=grid[0].size()-1)
            return false;
        if(v[grid.size()-1][grid[0].size()-1]==0)
            return false;
        return true;
    }
};

/*
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
*/