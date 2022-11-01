#include <string>
#include <vector>
#include<iostream>
#include<cmath>
using namespace std;

vector<vector<int>> keypad = {
        {2,4},
        {1,1},{2,1},{3,1},
        {1,2},{2,2},{3,2},
        {1,3},{2,3},{3,3},
        {1,4},{3,4}
};

int thumbMovement(int number, vector<vector<int>> hands) {
    int RtD = abs(keypad[number][0] - hands[0][0]) + abs(keypad[number][1] - hands[0][1]);
    int LtD = abs(keypad[number][0] - hands[1][0]) + abs(keypad[number][1] - hands[1][1]);
    if (RtD < LtD) return 1;
    else if (RtD > LtD) return 2;
    return  0;
}

string solution(vector<int> numbers, string hand) {
    string answer = "";
    vector<int> Rt = { 3, 4 };
    vector<int> Lt = { 1, 4 };
    int h = 0;
    if (hand == "right")
        h = 0;
    else
        h = 1;

    for (int i : numbers) cout << i << ' ';
    cout << endl;
    cout << hand << endl;
    for (int i : numbers) {
        vector<vector<int>> hands = {Rt,Lt};
        cout << i << ':';
        cout << "P(";
        for (int i : keypad[i]) cout << i << ' ';
        cout << "), RT( ";
        for (int i : Rt) cout << i << ' ';
        cout << "), LT( ";
        for (int i : Lt) cout << i << ' ';
        
        switch (i){
            case 3:case 6:case 9:
                answer += 'R';
                hands[0] = keypad[i];
                break;
            case 1: case 4: case 7:
                answer += 'L';
                hands[1] = keypad[i];
                break;
            default:
                switch (thumbMovement(i, hands))
                {
                case 0:
                    answer += hand[0] - 'a' + 'A';
                    hands[h] = keypad[i];
                    break;
                case 1:
                    answer += 'R';
                    hands[0] = keypad[i];
                    break;
                case 2:
                    answer += 'L';
                    hands[1] = keypad[i];
                    break;
                default:
                    break;
                } 
                break;
        }
        Rt = hands[0];
        Lt = hands[1];
        cout << ") " << answer.back() << endl;
    }

    return answer;
}

//int main() {
//    vector<int> num = { 7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2 };
//    string hand = "left";
//    cout << solution(num, hand);
//}