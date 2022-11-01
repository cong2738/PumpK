//#include<bits/stdc++.h>
//using namespace std;
//
//vector<int> solution(string s) {
//    vector<int> answer;
//    map<int, int> numMap;
//    vector<pair<int,int>> pairs;
//    string tmp = "";
//    for (char c : s) {
//        if (isdigit(c)) {
//            tmp += c;
//        }
//        else {
//            if (!tmp.empty()) {
//                numMap[stoi(tmp)]++;
//                tmp.clear();
//            }
//        }
//    }
//    for (auto it : numMap) {
//        pairs.push_back(pair<int, int>(it.second, it.first));
//    }
//    sort(pairs.begin(), pairs.end());
//    reverse(pairs.begin(), pairs.end());
//    for (auto i : pairs) {
//        answer.push_back(i.second);
//    }
//    return answer;
//}
//int main() {
//    string str = "{{2},{2,1},{2,1,3},{2,1,3,4}}";
//    solution(str);
//}