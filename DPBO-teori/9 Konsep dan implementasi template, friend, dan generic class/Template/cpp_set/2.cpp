#include <cstdio>
#include <vector>
#include <set>
#include <string>
using namespace std;

int main(){
	set<int> s;
	
	s.insert(7);
	s.insert(8);
	s.insert(7);
	s.insert(8);
	
	set<int>::const_iterator it;
	vector<int> str;
	int i=0;
	for(it = s.begin();it!=s.end();it++){
		str.push_back(0 + *it);
		printf("%d\n", str[i]);
		i++;
	}
	
	return 0;
}