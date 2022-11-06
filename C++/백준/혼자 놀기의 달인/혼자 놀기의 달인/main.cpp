using namespace std;
#include<bits/stdc++.h>

int solution(vector<int> cards) {
    int answer = 0;
    map<int, int> game;
    for (size_t i = 0; i < cards.size(); i++)
    {
        game[i + 1] = cards[i];
    }
    for (size_t box = 1; box <= cards.size(); box++)
    {
        int sum = 0;
        while (game[box] != 0) {
            int card = game[box];
            game[box] = 0;
            sum += card;
            box = card;
        }
        answer = max(sum, answer);
    }
    return answer;
}
int main() {
    vector<int>cards = { 8,6,3,7,2,5,1,4 };
    cout<<solution(cards);
}