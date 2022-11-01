//#include<bits/stdc++.h>
//using namespace std;
//int solution(int distance, vector<vector<int>> scope, vector<vector<int>> times) {
//    int answer = 1;
//    int numofgaurd = scope.size();
//    vector<bool> gaurd(numofgaurd, false);
//    for (auto& a1 : scope) {
//        sort(a1.begin(), a1.end());
//    }
//    while (answer < distance)
//    {
//        for (int i = 0; i < numofgaurd; i++) {
//            int x = (answer - 1) % (times[i][0] + times[i][1]);
//            if (x < times[i][0])
//                if (scope[i][0] <= answer && scope[i][1] >= answer)
//                    return answer;
//        }        
//        answer++;
//    }
//    return answer;
//}
//int main() {
//    int distance = 12;
//    vector<vector<int>> scope =
//    { {8, 7}, {4, 6}, {11, 10} };
//
//    vector<vector<int>> times = 
//    { {2, 2}, {2, 4}, {3, 3} };
//
//    cout<<solution(distance, scope, times);
//    return 0;
//}