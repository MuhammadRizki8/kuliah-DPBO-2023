#include <cstdio>
#include <vector>
#include <set>
#include <string>
using namespace std;

int main(){
	set<string> s;
	
	s.insert("Hello");
	s.insert("World");
	s.insert("Hello");
	s.insert("World2");
	
	set<string>::const_iterator it;
	vector<string> str;
	int i=0;
	for(it = s.begin();it!=s.end();it++){
		str.push_back("" + *it);
		printf("%s\n", str[i].c_str());
		i++;
	}
	
	return 0;
}