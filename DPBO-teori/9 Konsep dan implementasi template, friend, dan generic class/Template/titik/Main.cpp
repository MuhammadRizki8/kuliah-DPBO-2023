#include <cstdio>
#include <iostream>
using namespace std;
#include "Mesin.cpp"
#include "Titik.cpp"
#include "Tulis.cpp"

int main(){
	tulisMasukan(18);
	tulisMasukan(28.11);
	tulisMasukan("prosedur tulisMasukkan dengan masukan string");
	
	keluaran(11, 11.82);
	keluaran(9, 'A');
	keluaran(9.81,'A');
	keluaranO('A');
	keluaranO(81);
	keluaranO(82.81);
	keluaranO(3,5);
	keluaranO(18.9,28.11);
	
	
	Titik<double> t1(28.99,1);
	string kata = "membahas template";
	
	cout << "t1 : x : " << t1.getX() << " y : " << t1.getY() << endl;
	Tulis<string> t(kata);
	
	Titik<string> t2("aa","bb");
	cout << "t2 : x : " << t2.getX() << " y : " << t2.getY() << endl;
	
	
	return 0;
}