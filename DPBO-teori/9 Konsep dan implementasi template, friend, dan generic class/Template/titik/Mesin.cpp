template <class Masukan>
void tulisMasukan(Masukan n){
	cout << "masukan : " << n << endl;
}

template <class A, class B>
A keluaran(A n, B m){
	cout << "keluaran 2 tipe : " << n << m << endl;
	return n;
}

template <class T>
T keluaranO(T n){
	cout << "keluaran overloading : " << n << endl;
	return n;
}

template <class T>
T keluaranO(T x, T y){
	cout << "keluaran overloading : " << x << y << endl;
	return (x*y);
}