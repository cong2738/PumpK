//#include<map>
//#include<string>
//#include<vector>
//#include<algorithm>
//#include<iostream>
//using namespace std;
//
//vector<string> solution(vector<string> orders, vector<int> course) {
//    vector<string> answer;
//	for (string &vs : orders) {
//		sort(vs.begin(), vs.end());
//	}
//	for (int i : course) {	
//		map<string, int> cm;
//		for (string s : orders) {
//			int len = s.size();
//			if (len >= i) {
//				vector<bool> v(len - i, false);
//				v.insert(v.end(), i, true);
//				do {
//					string temp = "";
//					for (int k = 0; k < len; k++) {
//						if (v[k]) temp += s[k];
//					}
//					cm[temp]++;
//				} while (next_permutation(v.begin(), v.end()));
//			}
//		}
//		int maxnum = 0;
//		for (auto it : cm) 
//			maxnum = max(maxnum, it.second);
//		for (auto it : cm) 
//			if (maxnum > 1 && it.second == maxnum)
//				answer.push_back(it.first);
//	}
//	sort(answer.begin(), answer.end());
//    return answer;
//}
//int main() {
//    vector<string> orders = {
//        "ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"
//    };
//    vector<int> coutse = {
//        2,3,4
//    };
//    for (string i : solution(orders, coutse)) cout << i << ' ';
//}