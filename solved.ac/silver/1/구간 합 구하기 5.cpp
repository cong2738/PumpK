#include<iostream>
#include<vector>
using namespace std;

int main(){
    ios::sync_with_stdio(0); cin.tie(0);

    int N,M; cin >> N >> M;

    vector<vector<int>> prefix(1025,vector<int>(1025));
    for (int i = 0; i < N; i++) for (int j = 0; j < N; j++){
        int num; cin >> num;
        
        prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + num;
	}

	for (int i = 0; i < M; i++) {
		int x1, y1, x2, y2; cin >> y1 >> x1 >> y2 >> x2;
		cout << prefix[y2][x2] - prefix[y1 - 1][x2] - prefix[y2][x1 - 1] + prefix[y1 - 1][x1 - 1] << '\n';
	}

	return 0;
}
