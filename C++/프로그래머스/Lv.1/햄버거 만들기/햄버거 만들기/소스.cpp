#include<bits/stdc++.h>

using namespace std;

int solution(vector<int> ingredient) {
    int answer = 0;
    list<int> ind;
    list<int> hamburger = { 1,2,3,1 };
    for (int i : ingredient) ind.push_back(i);
    while (true) {
        int bf = ind.size();
        list<int>::iterator it1 = find(ind.begin(), ind.end(), hamburger), it2 = it1;
        advance(it2, 4);
        ind.erase(it1, it2);
        if (ind.size() == bf) break;
        else {
            answer++;
        }
    }
    return answer;
}
int main() {
    vector<int> ingredient = { 1, 3, 2, 1, 2, 1, 3, 1, 2 };
    cout<<solution(ingredient);
}
