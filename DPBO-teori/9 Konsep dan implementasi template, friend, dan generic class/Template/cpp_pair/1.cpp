#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main(){
	int n;
	scanf("%d", &n);
	pair<int, int> data[n];
	for(int i=0;i<n;i++){
		scanf("%d %d", &data[i].first, &data[i].second);
	}
	
	printf("isi data pair\n");
	for(int i=0;i<n;i++){
		printf("%d %d\n",data[i].first, data[i].second);
	}
	
	return 0;
}