#include<iostream>
#include<vector>
using namespace std;

#define MAX(A,B) A.size() >= B.size() ? A : B

int main(void){
    string A,B; cin>>A>>B;
    int AL = A.size(), BL = B.size();
    vector<vector<string>> LCS(A.size()+1,vector<string>(B.size()+1));
    for (size_t i = 0; i < A.size(); i++)
    {
        for (size_t j = 0; j < B.size(); j++)
        {
            if(A[i] == B[i]) LCS[i+1][j+1] = LCS[i][j] + A[i];
            else LCS[i+1][j+1] = MAX(LCS[i][j+1], LCS[i+1][j]);
        }
    }
    cout << LCS[AL][BL] << '\n' << LCS[AL][BL].size();
}