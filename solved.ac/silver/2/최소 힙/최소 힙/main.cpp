#include<bits/stdc++.h>
using namespace std;
int main() {
	int n,cmd;
	multiset<int> heap;
	ios::sync_with_stdio(false); cin.tie(NULL);
	cin >> n;
	for (size_t i = 0; i < n; i++) {
		cin >> cmd;
		switch (cmd)
		{
		case 0:
			if (!heap.empty()) {
				cout << *heap.begin() << '\n';
				heap.erase(heap.begin());				
			}
			else cout << 0 << '\n';
			break;
		default:
			heap.insert(cmd);
			break;
		}
	}
}