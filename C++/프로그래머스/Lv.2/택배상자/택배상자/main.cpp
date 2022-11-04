#include<bits/stdc++.h>
using namespace std;
int solution(vector<int> order) {
    int answer = 0;
    stack<int> convB;
    for (int i = 1; i <= order.size(); i++)
    {
        convB.push(i);
        while (!convB.empty() && order[answer] == convB.top()) {
            convB.pop();
            answer++;
        }
    }
    return answer;
}
int main() {
    vector<int> order = 
    { 5,4,3,2,1, };
    //{ 4, 3, 1, 2, 5 };
    cout<<solution(order);
}