#include <string>
#include <vector>
#include <iostream>
using namespace std;
//´äºÃÀ½ ¤µ¤² ±íÀÌ¿ì¼±Å½»ö ¾î·Æ³ë
int scoreResult = -1;
vector<int> ryan, apeach, ryanResult;

pair<int, int> calculate() {
    pair<int, int> score = { 0, 0 };
    for (int i = 0; i < 11; i++) {
        if (ryan[i] == apeach[i]) {
            if (ryan[i] == 0 && apeach[i] == 0) {
                continue;
            }
            else {
                score.second += (10 - i);
            }
        }
        else {
            if (ryan[i] > apeach[i]) {
                score.first += (10 - i);
            }
            else {
                score.second += (10 - i);
            }
        }
    }
    return score;
}

void check() {
    pair<int, int> score = calculate();
    int ryanScore = score.first;
    int apeachScore = score.second;
    int diff = ryanScore - apeachScore;
    if (diff <= 0) {
        return;
    }

    if (scoreResult == -1) {
        scoreResult = diff;
        ryanResult = ryan;
    }
    else {
        if (scoreResult == diff) {
            for (int i = 10; i >= 0; i--) {
                if (ryan[i] != 0 && ryanResult[i] == 0) {
                    ryanResult = ryan;
                    break;
                }
                else if (ryan[i] == 0 && ryanResult[i] != 0) {
                    break;
                }
                else if (ryan[i] != 0 && ryanResult[i] != 0) {
                    if (ryan[i] != ryanResult[i]) {
                        ryanResult = ryan[i] > ryanResult[i] ? ryan : ryanResult;
                        break;
                    }
                }
            }
        }
        else if (scoreResult < diff) {
            scoreResult = diff;
            ryanResult = ryan;
        }
    }
}

void dfs(int cnt, int idx, int n) {
    if (cnt == n) {
        check();
        return;
    }

    int curArrow = n - cnt;
    if (idx == 10) {
        ryan[idx] = curArrow;
        dfs(cnt + curArrow, idx + 1, n);
        ryan[idx] = 0;
    }
    else {
        if (apeach[idx] + 1 <= curArrow) {
            ryan[idx] = apeach[idx] + 1;
            dfs(cnt + apeach[idx] + 1, idx + 1, n);
            ryan[idx] = 0;
        }
        dfs(cnt, idx + 1, n);

    }
}

vector<int> solution(int n, vector<int> info) {
    ryan.resize(11, 0);
    apeach = info;
    dfs(0, 0, n);

    if (scoreResult == -1) {
        ryanResult.push_back(-1);
    }
    return ryanResult;
}

int main() {
    int n = 5;
    vector<int> info =
    { 2,1,1,1,0,0,0,0,0,0,0 };
    for (int i : solution(n, info)) cout << i << ' ';
}