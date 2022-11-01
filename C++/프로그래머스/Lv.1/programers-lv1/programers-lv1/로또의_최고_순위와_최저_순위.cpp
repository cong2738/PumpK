#include <string>
#include <vector>
#include<iostream>
using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    vector<int> count={0,0};
    int win = win_nums.size()+1;
    for (int i : lottos) {
        if (i == 0) count[0]++;
        for (int j : win_nums) {
            if (j == i) count[1]++;
        }
    }
    count[0] = count[0] + count[1];
    for (int i : count) {
        cout << i << endl;
        if (i > 0) {
            cout << "µ¥Âm\n";
            answer.push_back(win-i);
        }
        else answer.push_back(6);
    }
    return answer;
}
//int main() {
//    for (
//        int i : solution(
//                { 44, 1, 0, 0, 31, 25 }, { 31, 10, 45, 1, 6, 19 }
//            )
//        ) 
//        cout << i << ' ';
//}