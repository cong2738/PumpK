#include<bits/stdc++.h>
using namespace std;
vector<int> solution(string msg) {
    vector<int> answer;
    vector<string> test;
    map<string, int> alph = { {"",-1},{"A",1},{"B",2},{"C",3},{"D",4},{"E",5},{"F",6},{"G",7},{"H",8},{"I",9},{"J",10},{"K",11},{"L",12},{"M",13},{"N",14},{"O",15},{"P",16},{"Q",17},{"R",18},{"S",19},{"T",20},{"U",21},{"V",22},{"W",23},{"X",24},{"Y",25},{"Z",26} };    
    cout << alph.size() << endl;
    while (!(msg.empty())&&msg.length()!=1) {
        string word = ""; 
        string setting = "";
        int index = 1;
        while (alph.find(word)!=alph.end()) {
            setting = word;
            word = msg.substr(0, index++);            
        }
        answer.push_back(alph[setting]);
        alph[word] = alph.size();
        msg = msg.substr(setting.length());
    }
    if (!empty(msg)) answer.push_back(alph[msg]);
    return answer;
}
int main() {
    string msg = "ABABABABABABABAB";
    for (auto i : solution(msg)) cout << i << ' ';
}