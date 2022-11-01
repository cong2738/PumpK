//#include <string>
//#include <vector>
//#include<algorithm>
//#include<iostream>
//using namespace std;
//int solution(vector<int> people, int limit) {
//    int answer = 0;
//    int big = people.size() - 1;
//    int small = 0;
//    sort(people.begin(), people.end());
//    while (small <= big) {
//        int sum = people[small] + people[big];
//        if (sum > limit) {
//            big--;
//        }
//        else if (sum <= limit) {
//            big--;
//            small++;
//        }
//        answer++;
//    }
//    return answer;
//}
//int main() {
//    cout<<solution({ 70, 50, 80, 50 }, 100);
//}