//#include<bits/stdc++.h>
//using namespace std;
//int solution(int k, vector<vector<int>> dungeons) {
//    int answer = 0;
//    sort(dungeons.begin(), dungeons.end());    
//    string s = "";
//    for (size_t i = 0; i < dungeons.size(); i++)
//    {
//        s += i + '0';
//    }
//    int len = dungeons.size();
//    vector<vector<vector<int>>> comb;
//    do {
//        vector<vector<int>> tmp;
//        for (int i = 0; i < len; i++) {
//            tmp.push_back(dungeons[i]);
//        }
//        comb.push_back(tmp);
//    } while (next_permutation(dungeons.begin(), dungeons.end()));
//    for (auto X : comb) {
//        int tmp = 0;
//        int piro = k;
//        for (auto v : X) {            
//            if (piro >= v[0]) {
//                piro -= v[1];
//                tmp++;
//            }
//            answer = max(answer, tmp);
//            if (piro <= 0) {                
//                break;
//            }
//        }
//    }
//    
//    return answer;
//}
using namespace std;
#include<vector>
#include<iostream>
int solution(int k, vector<vector<int>> dungeons) {
    int ans = 0;
    for (auto it = dungeons.begin(); it != dungeons.end(); it++) {
        vector<vector<int>> d2( dungeons.begin(), it );       
        if (k >= (*it)[0]) {
            d2.insert(d2.end(), it + 1, dungeons.end());
            int s = solution(k - (*it)[1], d2) + 1;
            ans = s > ans ? s : ans;
        }
    }
    return ans;
}
int main() {
    int k = 80;
    vector<vector<int>> dungeons = { {80,20},{50,40},{30,10} };
    cout << solution(k, dungeons);
}