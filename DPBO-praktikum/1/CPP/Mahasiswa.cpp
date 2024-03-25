//library yang dipakai
#include<iostream>
#include<string>
//standar library
using namespace std;

class Mahasiswa
{
    //variabel private
private:
    string name;
    string nim;
    string prodi;
    string fakultas;

public:
    //constructor
    Mahasiswa(){
        this->name="";
        this->nim="";
        this->prodi="";
        this->fakultas="";
    }
    // construktor
    Mahasiswa(string name, string nim, string prodi, string fakultas)
    {
        this->name = name;
        this->nim = nim;
        this->prodi = prodi;
        this->fakultas = fakultas;
    }

    string get_name() {
        return this->name;
    }

    string get_nim() {
        return this->nim;
    }

    string get_prodi() {
        return this->prodi;
    }

    string get_fakultas() {
        return this->fakultas;
    }

    void set_name(string name) {
        this->name = name;
    }

    void set_nim(string nim) {
        this->nim = nim;
    }

    void set_prodi(string prodi) {
        this->prodi = prodi;
    }

    void set_fakultas(string fakultas) {
        this->fakultas = fakultas;
    }
    //destructor
    ~Mahasiswa()
    {

    }
};
