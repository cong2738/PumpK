#include<bits/stdc++.h>
using namespace std;
vector<int> solution(string msg) {
    vector<int> answer;
    deque<char> mq(msg.begin(), msg.end());
    map<string, int> alph = { {"",-1},{"A",1},{"B",2},{"C",3},{"D",4},{"E",5},{"F",6},{"G",7},{"H",8},{"I",9},{"J",10},{"K",11},{"L",12},{"M",13},{"N",14},{"O",15},{"P",16},{"Q",17},{"R",18},{"S",19},{"T",20},{"U",21},{"V",22},{"W",23},{"X",24},{"Y",25},{"Z",26} };            
    string c;
    while (!mq.empty()&&mq.size()!=1) {
        string w = "";
        while (alph.find(w + c) != alph.end()) {
            w += mq.front();
            mq.pop_front();
            c = mq.front();
        }
        alph[w + c] = alph.size();
        answer.push_back(alph[w]);
    }    
    if (!mq.empty()) answer.push_back(alph[string(1, mq[0])]);
    return answer;
}
int main() {
    string msg = "KAKAO";
    for (auto i : solution(msg)) cout << i << ' ';
}