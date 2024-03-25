#include <cstdio>
#include <iostream>
using namespace std;
#include "Mesin.cpp"
#include "Aritmatika.cpp"
#include "Tulis.cpp"

int main(){
	int x,y;
	// while (true){
		Aritmatika<double> t1(1,2);
		string kata = "Latihan Aritmatika";
		// cout<<"Masukan nilai x : ";cin>>x;
		// cout<<"Masukan nilai y : ";cin>>y;
		cout << "Operasi 1\nx : " << t1.getX() << " y : " << t1.getY() << endl;
		cout << "x + y =" << t1.tambah()<< endl;
		cout << "x - y =" << t1.kurang()<< endl;
		cout << "x * y =" << t1.kali()<< endl;
		cout << "x / y =" << t1.bagi()<< endl;
		Tulis<string> t(kata);
	
		Aritmatika<string> t2("aa","bb");
		cout << "t2 : x : " << t2.getX() << " y : " << t2.getY() << endl;
		// cout << "x + y =" << t2.tambah()<< endl;
		// cout << "x - y =" << t2.kurang()<< endl;
		// cout << "x * y =" << t2.kali()<< endl;
		// cout << "x / y =" << t2.bagi()<< endl;

	// };
	// tulisMasukan(18);
	// tulisMasukan(28.11);
	// tulisMasukan("Program Aritmatika");
	
	// keluaran(11, 11.82);
	// keluaran(9, 'A');
	// keluaran(9.81,'A');
	// keluaranO('A');
	// keluaranO(81);
	// keluaranO(82.81);
	// keluaranO(3,5);
	// keluaranO(18.9,28.11);
	
	
	
	
	return 0;
}