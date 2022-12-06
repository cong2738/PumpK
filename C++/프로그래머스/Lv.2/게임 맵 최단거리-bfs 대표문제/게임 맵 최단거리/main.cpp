#include<bits/stdc++.h>
using namespace std;

int bfs(vector<vector<int>>maps) {   
    const vector<int>
        dx = { -1,1,0,0 },
        dy = { 0,0,-1,1 };
    int n = maps.size(),
        m = maps[0].size();
    queue<pair<int, int>> q({ {0,0} });
    vector<vector<int>> ret(n,vector<int>(m,0));
    while (!q.empty()) {
        pair<int, int> loc = q.front(); q.pop();
        for (size_t i = 0; i < 4; i++) {
            int nX = loc.first + dx[i],
                nY = loc.second + dy[i],
                inRange = 0 <= nX && nX <= n - 1 && 0 <= nY && nY <= m - 1;
            if (inRange && maps[nX][nY]) {
                q.push({ nX,nY });
                maps[nX][nY] = 0;
                ret[nX][nY] = ret[loc.first][loc.second] + 1;
            }
        }
    }
    if (ret.back().back()) return ret.back().back() + 1;
    else return -1;
}
int solution(vector<vector<int> > maps) {
    return bfs(maps);
}
int main() {
    vector<vector<int>> maps = { 
        {1,0,1,1,1},
        {1,0,1,0,1},
        {1,0,1,1,1},
        {1,1,1,0,1},
        {0,0,0,0,1} 
    };
    cout << solution(maps);
}