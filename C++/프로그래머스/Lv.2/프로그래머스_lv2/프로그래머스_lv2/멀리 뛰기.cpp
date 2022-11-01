//#include<iostream>
//#include <vector>
//using namespace std;
//vector<int> memo ={1,1,2};
//int jump(int n) {
//    if (n == 0) return memo[0];
//    else if (n == 1) return memo[1];
//    else if (n == 2) return memo[2];
//    else if (memo[n] != 0) return memo[n];
//    else {
//        memo[n] = jump(n - 1) + jump(n - 2);
//        return memo[n];
//    }
//}
//long long solution(int n) {
//    memo.resize(n+1,0);
//    return jump(n);
//}
//int main() {
//
//    cout << solution(5);
//}