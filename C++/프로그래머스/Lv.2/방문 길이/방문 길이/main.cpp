#include<bits/stdc++.h>
using namespace std;
int solution(string dirs) {
    vector<int> point = { 0,0 };
    set<set<vector<int>>> rodes;
    for (char cmd : dirs) {
        set<vector<int>>rode;
        vector<int> nextP;
        switch (cmd)
        {
        case 'U':
            if (point[1] < 5) {
                nextP = { point[0],point[1] + 1 };
                rode.insert(point);
                rode.insert(nextP);
                point = nextP;
                rodes.insert(rode);
            }
            break;
        case 'D':
            if(point[1]>-5) {
                nextP = { point[0],point[1]-1 };
                rode.insert(point);
                rode.insert(nextP);
                point = nextP;
                rodes.insert(rode);
            }
            break;
        case 'R':
            if(point[0]<5) {
                nextP = { point[0] + 1, point[1] };
                rode.insert(point);
                rode.insert(nextP);
                point = nextP;
                rodes.insert(rode);
            }
            break;
        case 'L':
            if(point[0]>-5) {
                nextP = { point[0] - 1, point[1] };
                rode.insert(point);
                rode.insert(nextP);
                point = nextP;
                rodes.insert(rode);
            }
            break;
        default:
            break;
        }
    }
    return rodes.size();
}
int main() {
    string dirs = "ULURRDLLU";
    cout << solution(dirs);
    return 0;
}