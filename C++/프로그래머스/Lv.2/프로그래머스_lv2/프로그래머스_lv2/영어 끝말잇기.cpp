//#include <string>
//#include <vector>
//#include <iostream>
//#include<algorithm>
//
//using namespace std;

//vector<int> solution(int n, vector<string> words) {
//    vector<string> p;
//    char ec = words[0].front();
//    for (int i = 0; i < words.size(); i++)
//    {
//        int f = find(p.begin(), p.end(), words[i]) - p.begin();
//        if (words[i].front() != ec || f != p.size()) 
//            return { (i) % n + 1, (i) / n };
//        p.push_back(words[i]);
//        ec = words[i].back();
//    }
//    return { 0,0 };
//}
//int main() {
//    vector<string> word = {
//        "tank", "kick", "know", 
//        "wheel", "land", "dream", 
//        "mother", "robot", "tank"
//    };
//    int n = 3;
//    for (int i : solution(n, word)) {
//        cout<< i << ' ' ;
//    }
//}