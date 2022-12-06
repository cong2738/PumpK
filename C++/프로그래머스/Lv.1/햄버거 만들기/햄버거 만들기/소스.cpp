#include<bits/stdc++.h>
using namespace std;
int solution(vector<int> ingredient) {
    int answer = 0;
    deque<int> hamburger, recipe = {1,2,3,1};
    for (int i : ingredient) {
        hamburger.push_back(i);        
        auto itback = hamburger.end();
        if (hamburger.size() >= 4 && deque<int>(itback - 4, itback) == recipe) {
            for (size_t i = 0; i < 4; i++) hamburger.pop_back();
            answer++;
        }
    }
    return answer;
}

int main() {
    vector<int> ind = { 2, 1, 1, 2, 3, 1, 2, 3, 1 };
    cout<<solution(ind);
}
