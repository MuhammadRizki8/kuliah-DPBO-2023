//library yang dipakai
#include <iostream>
#include <string>
#include <list>
#include <array>
//standar library
using namespace std;

class Tabel
{
private:
    int baris;
    int kolom;
public:
//constructor
    Tabel(){

    }
    Tabel(int baris, int kolom){
        this->baris=baris;
        this->kolom=kolom;
    }
    void set_baris(int baris) {
        this->baris = baris; 
    }
    void set_kolom(int kolom) {
        this->kolom = kolom; 
    }
    int get_baris() { 
        return baris; 
    }
    int get_kolom() {
        return kolom; 
    }
    //menampilkan isi objek dalam bentuk sebaris tabel
    void buat_baris(array<string, 4> isi, int max[4], int line, char type_line) {
        for (int i = 0; i < line + 13; i++) {//menampilkan garis atas
            cout << type_line;
        }
        cout<<endl;
        cout << "| ";
        for (int i = 0; i < this->kolom; i++) {//menampilkan isi perkolom
            cout <<isi[i];
            for (int j = 0; j < max[i] - isi[i].length(); j++) {//menampilkan spasi
                cout << " ";
            }
            cout<<" | ";
        }
        cout << endl;
        for (int i = 0; i < line + 13; i++) {//menampilkan garis bawah
            cout << type_line;
        }
        cout << endl;
    }
    //destructor
    ~Tabel(){

    }
};

