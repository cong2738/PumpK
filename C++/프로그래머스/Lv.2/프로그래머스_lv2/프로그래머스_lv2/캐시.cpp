//#include <string>
//#include <vector>
//#include<list>
//#include<algorithm>
//#include<iostream>
//using namespace std;
//
//int solution(int cacheSize, vector<string> cities) {
//    int answer = 0;
//    list<string>cache;
//    for (int i = 0; i < cities.size(); i++)
//    {
//        for (int j = 0; j < cities[i].length(); j++)
//        {
//            char c = cities[i][j];
//            if (c >= 'A' && c<='Z') cities[i][j] += -'A' + 'a';
//        }
//    }
//    for (string s1 : cities) {
//        auto it = find(cache.begin(), cache.end(), s1);
//        if (it != cache.end()) {
//            cache.splice(cache.end(), cache, it);
//            answer++;
//        }
//        else if(cache.size() == cacheSize) {
//            cache.push_back(s1);
//            cache.pop_front();
//            answer += 5;
//        }
//        else {
//            cache.push_back(s1);
//            answer += 5;
//        }
//    }
//    return answer;
//}
//int main() {
//    vector<string>cities = {
//        "Jeju", "Pangyo", "NewYork", "newyork"
//    };
//    int n = 3;
//    cout << solution(n,cities);
//}