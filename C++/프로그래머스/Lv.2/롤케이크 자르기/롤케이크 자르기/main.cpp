#include<bits/stdc++.h>
using namespace std;

int solution(vector<int> topping) {
    int answer = 0;
    map<int, int> OB;
    map<int, int> YB;
    for (int i : topping) {
        OB[i]++;
    }
    for (int i : topping) {
        YB[i]++;
        OB[i]--;
        if (OB[i] == 0) {
            OB.erase(i);
        }
        answer += OB.size() == YB.size();
    }
    return answer;
}
int main() {
    vector<int> topping = {1, 2, 1, 3, 1, 4, 1, 2};
    cout<<solution(topping)<<endl;
    return 0;
}