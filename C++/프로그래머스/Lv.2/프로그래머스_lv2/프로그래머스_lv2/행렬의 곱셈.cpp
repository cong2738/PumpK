//#include<bits/stdc++.h>
//using namespace std;
//
//vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
//    vector<vector<int>> answer;
//    for (vector<int> V1 : arr1) {
//        vector<int> line;
//        for (int j = 0; j < arr2[0].size(); j++)
//        {   
//            int n = 0;
//            for (int i = 0; i < arr2.size(); i++)
//            {
//                n += V1[i] * arr2[i][j];
//            }
//            line.push_back(n);
//        }
//        answer.push_back(line);
//    }
//    return answer;
//}