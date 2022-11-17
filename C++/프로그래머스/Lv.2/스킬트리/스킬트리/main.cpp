#include<bits/stdc++.h>
using namespace std;
int ganeung(string skTree, deque<char>rq) {
    for (char sk : skTree) {
        if (rq.empty()) break;
        auto f = find(rq.begin(), rq.end(), sk);
        if (sk == rq.front()) rq.pop_front();
        else if (f != rq.end()) return 0;
    }
    return 1;
}
int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    deque<char> rq;
    for (char sk : skill) rq.push_back(sk);
    for (string st : skill_trees) {
        answer += ganeung(st, rq);
    }
    return answer;
}
int main() {
    string skill = "CBD";
    vector<string> skill_trees = { "BACDE", "CBADF", "AECB", "BDA" };
    cout << solution(skill, skill_trees);
    return 0;
}