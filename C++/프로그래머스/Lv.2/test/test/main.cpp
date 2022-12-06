#include<bits/stdc++.h>
using namespace std;
int main() {
	tuple<int, int, int, int>tp( 1,2,3,4 );
	int n = tuple_size<decltype(tp)>::value;
	return 0;
}