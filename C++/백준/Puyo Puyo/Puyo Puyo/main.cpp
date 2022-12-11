#include <bits/stdc++.h>
using namespace std;

vector<string> board(12);
const int n[4][2] = { {0,1},{0,-1},{1,0},{-1,0} };

void findchar(int x, int y, int* count, vector<vector<int>>* visited, vector<vector<int>>* tmp) {
	(*count)++;
	(*tmp).push_back({ x,y });
	(*visited)[y][x] = 1;
	for (auto p : n) {
		int ny = y + p[0],
			nx = x + p[1];		
		if (0 <= ny && ny < 12 && 0 <= nx && nx < 6) {			
			if (!(*visited)[ny][nx] && board[ny][nx] == board[y][x]) {				
				findchar(nx, ny, count, visited, tmp);
			}
		}
	}
}
bool bbayoen(int count, vector<vector<int>> storage) {
	if (count < 4) return false;
	for (auto p : storage) {
		board[p[1]][p[0]] = '.';
	}
	return true;
}
int main() {
	char blockcolor[5] = { 'R','G','B','P','Y' };	
	for (string& s : board) cin >> s;
	int count = 0, bb = -1;
	while (true) {
		bb = 0;
		for (size_t x = 0; x < 6; x++) for (size_t y = 0; y < 12; y++) {
			if (board[y][x] != '.') {
				int Ccount = 0;
				vector<vector<int>> storage;
				vector<vector<int>>visited(12, vector<int>(6));
				findchar(x, y, &Ccount, &visited, &storage);
				bb += bbayoen(Ccount, storage);
			}
		}
		for (size_t x = 0; x < 6; x++) {
			deque<char> tmp;
			for (size_t y = 0; y < 12; y++) {
				if (board[y][x] != '.') tmp.push_front(board[y][x]);
				board[y][x] = '.';
			}
			int yindex = 11;
			for (auto c : tmp) {
				board[yindex--][x] = c;
			}
		}
		if (bb > 0) count++;
		else break;
	}
	cout << count;
}