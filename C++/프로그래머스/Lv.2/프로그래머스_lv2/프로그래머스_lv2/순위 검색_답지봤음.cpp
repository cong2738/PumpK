//#include<bits/stdc++.h>
//#include<unordered_map>
//using namespace std;
///*
//�������� info�� �޾� �ش� ������ ���ü��ִ� ���ɾ�('-') ���¸� ��� �ľ��� �ʿ� Ű�� �����ϰ� �������Ϳ� ������ �߰��Ѵ�.
//�����ڼ� * (2*2*2*2)��
//(���� ��� "�� ������ �ܰ��� 200" ��� { ["��--"], ["�Ͼ�����-"], ~~~ }�� 2*2*2�� Ű�� �������Ϳ� 200�� �߰��ϰԵȴ�.
//���� ���� �����ڰ� ���� ���°� �����Ҷ� ������� "�� ������ �ܰ��� 200"���Ŀ� �� ������ ������ 150"�� ���� ���
//"�Ͼ���-" ��� ���� ���°� �����ϰ� �̶� ���� ������ Ű�� "�Ͼ���-"�� �������Ϳ� 150�� �߰��Ѵ�.)
//
//answer���� query���� ���ǿ� �ش��ϴ� ���ڿ��� ������ �̰� ��[����]�� ���Ϳ��� ������ �������� ����Ž���Ͽ� ū ���� ������ ��ȯ�Ѵ�.
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