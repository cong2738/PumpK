using namespace std;
#include<bits/stdc++.h>

int solution(vector<int> cards) {
    int answer = 1;
    vector<int> NOCcomb(1);
    for (size_t box = 1; box <= cards.size(); box++)
    {
        int NOC = 0;
        while (cards[box - 1] != 0) {
            int card = cards[box - 1];
            cards[box - 1] = 0;
            box = card;
            NOC++;
        }
        NOCcomb.push_back(NOC);
    }
    sort(NOCcomb.begin(), NOCcomb.end(), greater<int>());
    return NOCcomb[0] * NOCcomb[1];
}
int main() {
    vector<int>cards = { 2,3,1 };
    cout << solution(cards);
}