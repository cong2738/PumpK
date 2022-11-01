//#include<bits/stdc++.h>
//using namespace std;
//
//vector<int> solution(vector<int> progresses, vector<int> speeds) {
//    vector<int> answer;
//    int n = progresses.size();
//    queue<int> progress;
//    queue<int> speed;
//    for (size_t i = 0; i < n; i++)
//    {
//        progress.push(progresses[i]);
//        speed.push(speeds[i]);
//    }
//    int date = 1;
//    int datanum = 0;
//    while (!progress.empty()) {
//        while (!progress.empty() && progress.front() + date * speed.front() >= 100) {
//            progress.pop();
//            speed.pop();
//            datanum++;
//        }
//        if (datanum != 0) {
//            answer.push_back(datanum);
//            datanum = 0;
//        }
//        date++;
//    }
//    return answer;
//}
//int main() {
//    vector<int> pro = { 93, 30, 55 };
//    vector<int> sp = { 1, 30, 5 };
//    for (int i : solution(pro, sp)) cout << i << ' ';
//}