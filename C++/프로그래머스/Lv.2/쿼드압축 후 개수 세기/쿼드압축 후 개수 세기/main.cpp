#include<bits/stdc++.h>
using namespace std;
vector<vector<int>> divSq(vector<vector<int>>arr, vector<int> xy) {
    int x = xy[0], y = xy[1], n = arr.size() >> 1;
    vector<vector<int>> ret(n, vector<int>(n));    
    for (size_t i = 0; i < n; i++) for (size_t j = 0; j < n; j++)
        ret[i][j] = arr[i + x][j + y];
    return ret;
}
bool same(vector<vector<int>> arr) {
    int bit = arr[0][0], n = arr.size();;
    for (auto v : arr) for (int i : v) 
        if (bit != i) return false;
    return true;
}
void qdZip(vector<vector<int>> arr, vector<int>* ct) {    
    int n = arr.size();
    if (same(arr)) (*ct)[arr[0][0]]++;
    else {
        vector<vector<int>> point = { { 0,0 } , { 0,n>>1 } , { n>>1,0 } , { n>>1,n>>1 } };
        for (auto v : point) qdZip(divSq(arr, v), ct);
    }
}
vector<int> solution(vector<vector<int>> arr) {
    vector<int>ct = { 0,0 };
    qdZip(arr,&ct);
    return ct;
}
int main() {
    vector<vector<int>> arr = { {1,1,0,0},{1,0,0,0},{1,0,0,1},{1,1,1,1} };
    for (auto i : solution(arr))cout << i<<' ';
    return 0;
}