//#include<bits/stdc++.h>
//#include<unordered_map>
//using namespace std;
///*
//지원자의 info를 받아 해당 조건의 나올수있는 돈케어('-') 형태를 모두 파악해 맵에 키로 저장하고 벨류벡터에 점수를 추가한다.
//지원자수 * (2*2*2*2)개
//(예를 들어 "니 엄마는 외계인 200" 라면 { ["니--"], ["니엄마는-"], ~~~ }의 2*2*2개 키의 벨류벡터에 200을 추가하게된다.
//또한 다음 지원자가 같은 형태가 존재할때 예를들어 "니 엄마는 외계인 200"이후에 니 엄마는 우주인 150"가 들어온 경우
//"니엄마-" 라는 공통 형태가 존재하고 이때 같은 형태의 키인 "니엄마-"의 정수벡터에 150을 추가한다.)
//
//answer값은 query에서 조건에 해당하는 문자열과 점수를 뽑고 맵[조건]의 벡터에서 점수를 기준으로 이진탐색하여 큰 값의 갯수를 반환한다.
//*/
//
//unordered_map< string, vector<int> > scores;
//
//void addCase(vector<string> s, int score) {
//	cout << endl << endl << s[0]<<s[1]<<s[2]<<s[3]<<score << endl;
//	for (int i = 0; i < 16; i++)
//	{
//		string str = "";
//		int a = i;
//		for (int j = 3; j >= 0; j--)
//		{
//			if (a <= 0 || a % 2 == 0) str = '-' + str;
//			else str = s[j] + str;
//			a /= 2;
//		}
//		cout << str << endl;
//		scores[str].push_back(score);
//	}
//}
//vector<int> solution(vector<string> info, vector<string> query) {
//	vector<int> answer;
//	vector<string> s(4); 
//	string str = "";
//	for (int i = 0; i < info.size(); i++) {
//		istringstream iss(info[i]);
//		iss >> s[0] >> s[1] >> s[2] >> s[3] >> str;
//		addCase(s, (int)stoi(str));
//	}
//	
//	for (auto it = scores.begin(); it != scores.end(); it++)
//		sort(it->second.begin(), it->second.end());
//	for (int i = 0; i < query.size(); i++) {
//		int score;
//		istringstream iss(query[i]);
//		iss >> s[0] >> str >> s[1] >> str >> s[2] >> str >> s[3] >> str;
//		score = stoi(str);
//		vector<int> v = scores[s[0] + s[1] + s[2] + s[3]];
//		if (v.size() != 0) {
//			auto it = lower_bound(v.begin(), v.end(), score);
//			answer.push_back(v.size() - (it - v.begin()));
//		}
//		else answer.push_back(0);
//	}
//	return answer;
//}
//int main() {
//	vector<string> info = {
//		"java backend junior pizza 150",
//		"python frontend senior chicken 210",
//		"python frontend senior chicken 150",
//		"cpp backend senior pizza 260",
//		"java backend junior chicken 80",
//		"python backend senior chicken 50"
//	};
//	vector<string> q = {
//		"java and backend and junior and pizza 100",
//		"python and frontend and senior and chicken 200",
//		"cpp and - and senior and pizza 250",
//		"- and backend and senior and - 150",
//		"- and - and - and chicken 100",
//		"- and - and - and - 150"
//	};
//	solution(info, q);
//}