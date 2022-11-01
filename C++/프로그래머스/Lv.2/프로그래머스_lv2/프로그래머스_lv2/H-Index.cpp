//#include <string>
//#include <vector>
//#include<iostream>
//#include<algorithm>
//using namespace std;
//
//int solution(vector<int> citations) {
//    int answer = 0;
//    int n = citations.size();
//    sort(citations.begin(), citations.end());
//    for (int i = 0; i < n; i++)
//    {
//        int hindex = n - i;
//        if (citations[i] >= hindex) {
//            answer = hindex;
//            break;
//        }
//    }
//    return answer;
//}
//int main() {
//    vector<int> citations = {
//        6,6,4,3,2,1
//    };
//    cout << solution(citations);
//}