#include<bits/stdc++.h>

using namespace std;

//vector<int> solution(string s) {
//    vector<int> answer(2);
//    int numofone = 0;
//    while (numofone != 1) {
//        numofone = count(s.begin(), s.end(), '1');
//        answer[0]++;
//        answer[1] += s.size() - numofone;
//        int tmp = numofone;
//        s = "";
//        while (tmp != 0) {
//            s += '0' + tmp % 2;
//            tmp = tmp >> 1;
//        }
//        if (numofone == 0) return { 0,1 };
//    }
//    return answer;
//}
//int main() {
//    vector<int> sol = solution("110010101001");
//    cout << sol[0] << ' '<<sol[1];
//}