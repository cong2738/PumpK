#include<bits/stdc++.h>
using namespace std;
int solution(int m, int n, vector<string> board) {
    int answer = 0;
    while(true) {
        vector<vector<int>> cmd;
        for (int i = 0; i < board.size() - 1; i++)
        {
            for (int j = 0; j < board[i].size() - 1; j++)
            {
                if (board[i][j] != ' ' && board[i][j] == board[i][j + 1] && board[i][j] == board[i + 1][j] && board[i][j] == board[i + 1][j + 1]) {
                    cmd.push_back({ i,j });
                }
            }
        }
        if (cmd.empty()) break;
        for (auto i : cmd) {
            board[i[0]][i[1]] = ' ';
            board[i[0]+1][i[1]] = ' ';
            board[i[0]][i[1]+1] = ' ';
            board[i[0]+1][i[1]+1] = ' ';
        }
        vector<string> newBoard(m, string(n, ' '));
        for (int i = 0; i < n; i++)
        {
            int gr = m - 1;
            for (int j = m - 1; j >= 0; j--)
            {
                if (board[j][i] != ' ') {
                    newBoard[gr][i] = board[j][i];
                    gr--;
                }
            }
        }
        board = newBoard;
    }    
    for (string s : board) answer += count(s.begin(),s.end(), ' ');
    return answer;
}
int main() {
    int m = 4, n = 5;
    vector<string> board = { 
        "CCBDE", 
        "AAADE", 
        "AAABF", 
        "CCBBF" 
    };
    cout << solution(m, n, board);
}