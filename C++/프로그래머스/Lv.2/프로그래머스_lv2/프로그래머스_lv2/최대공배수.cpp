//#include <string>
//#include <vector>
//#include<iostream>
//using namespace std;
//int gcd(int a, int b) {
//    return b ? gcd(b, a % b) : a;
//}
//int solution(vector<int> arr) {
//    int a = gcd(arr[0], arr[1]);
//    for (int i = 0; i < arr.size()-1; i++)
//    {
//        arr[i + 1] = arr[i] * arr[i + 1] / gcd(arr[i], arr[i + 1]);
//    }
//    return arr.back();
//}
//int main() {
//    cout<<solution({ 4,8,12,24 });
//}