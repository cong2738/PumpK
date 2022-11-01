//#include<bits/stdc++.h>
//using namespace std;
//
//int solution(vector<int> priorities, int location) {
//    vector<int>vc;
//    map<int, int> mp;
//    for (size_t i = 0; i < priorities.size(); i++)
//    {
//        mp[priorities[i]] = i;
//    }
//    for (auto it : mp) {
//        vc.push_back(it.second);
//    }
//    reverse(vc.begin(), vc.end());
//    return vc[location];
//}
//int main() {
//    vector<int> pri = { 2, 1, 3, 2 };
//    int loc = 2;
//    cout<<solution(pri, loc);
//}
