#include<bits/stdc++.h>
using namespace std;
int solution(vector<vector<int> > land)
{
    int answer = 0;
    for (size_t m = 0; m < land[0].size(); m++)
    {
        int sum = 0;        
        sum += land[0][m];
        int X = m;
        for (size_t i = 1; i < land.size(); i++)
        {
            int big = 0, tmp=X;            
            for (size_t j = 0; j < land[i].size(); j++)
            {
                if (X != j && land[i][j] > big) {
                    big = land[i][j];
                    tmp = j;
                }
            }
            X = tmp;
            sum += big;
        }
        answer = max(answer, sum);
    }
    return answer;
}
int main() {
    vector<vector<int>> land = { 
        {1,2,3,5},
        {5,6,7,100},
        {4,3,2,1} 
    };
    cout << solution(land);
    return 0;
}