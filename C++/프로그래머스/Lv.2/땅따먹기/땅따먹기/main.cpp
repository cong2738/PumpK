#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int> > land){
    for (int i = 0; i < land.size() - 1; i++) {
        land[i + 1][0] += max(land[i][1], max(land[i][2], land[i][3]));
        land[i + 1][1] += max(land[i][0], max(land[i][2], land[i][3]));
        land[i + 1][2] += max(land[i][0], max(land[i][1], land[i][3]));
        land[i + 1][3] += max(land[i][0], max(land[i][1], land[i][2]));
    }
    for (auto p : land) {
        for (int i : p) cout << i << '\t';
        cout << endl;
    }
    return *max_element(land.back().begin(), land.back().end());
}
int main() {
    vector<vector<int>> land = { 
        {1,2,3,5},
        {5,6,7,100},
        {4,3,2,1},
    };
    cout << solution(land);
    return 0;
}