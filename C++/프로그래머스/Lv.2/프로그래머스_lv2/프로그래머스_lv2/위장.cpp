//#include<bits/stdc++.h>
//
//using namespace std;
//int solution(vector<vector<string>> clothes) {
//    int answer = 1;
//    map<string, int> clm;
//    for (auto i : clothes) {
//        clm[i[1]]++;
//    }
//    for (auto it : clm) {
//        answer *= it.second + 1;
//    }
//    return answer-1;
//}