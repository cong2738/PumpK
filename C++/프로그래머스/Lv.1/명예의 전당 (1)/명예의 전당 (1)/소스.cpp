#include<bits/stdc++.h>
using namespace std;
vector<int> solution(int k, vector<int> score) {
    vector<int> ret;
    multiset<int> goat;
    for (int sc : score) {
        goat.insert(sc);  
        if (goat.size() > k) goat.erase(goat.begin());
        ret.push_back(*goat.begin());
    }
    return ret;
}
int main() {
    solution(3, { 10, 100, 20, 150, 1, 100, 200 });
}