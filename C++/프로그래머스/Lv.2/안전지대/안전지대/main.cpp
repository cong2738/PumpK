#include<bits/stdc++.h>
using namespace std;
int solution(vector<vector<int>> board) {
	int answer = 0,
		n = board.size(),
		m = board[0].size(),
		np[9][2] = { {0,0},{0,1},{0,-1},{1,0},{1,1},{1,-1},{-1,0},{-1,1},{-1,-1} };
	vector<vector<int>> DA(n, vector<int>(m));
	for (size_t i = 0; i < n; i++) {
		for (size_t j = 0; j < m; j++) {
			if (board[i][j]) {
				for (auto p : np) {
					int ni = i + p[0], nj = j + p[1];
					if (0 <= ni && ni < n && 0 <= nj && nj < m) DA[ni][nj] = 1;
				}
			}
		}
	}
	for (auto L : DA) answer += count(L.begin(), L.end(), 0);
	return answer;
}
int main() {
	vector<vector<int>> L = { 
		{0, 0, 0, 0, 0}, 
		{0, 0, 0, 0, 0}, 
		{0, 0, 0, 0, 0}, 
		{0, 0, 1, 0, 0}, 
		{0, 0, 0, 0, 0} 
	};
	cout << solution(L) << endl;
}