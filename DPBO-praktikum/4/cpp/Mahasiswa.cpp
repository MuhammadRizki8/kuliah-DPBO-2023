// memanggil file header
#include "header.hh"

// constructor kosong
Mahasiswa::Mahasiswa(){
    
}

// construktor berparameter
Mahasiswa::Mahasiswa(string nik,string nim, string nama, string jenis_kelamin, string prodi, string fakultas, string asal_universitas, string email_edu)
: SivitasAkademik(nik, nama, jenis_kelamin, asal_universitas, email_edu) {
this->nim = nim;
this->fakultas = fakultas;
this->prodi = prodi;
}

// ambil nilai nim
string Mahasiswa::get_nim() {
    return nim;
}

// mengisi nilai nim
void Mahasiswa::set_nim(string nim) {
    this->nim = nim;
}

// ambil nilai fakultas
string Mahasiswa::get_fakultas() {
    return fakultas;
}

// mengisi nilai fakultas
void Mahasiswa::set_fakultas(string fakultas) {
    this->fakultas = fakultas;
}

// ambil nilai prodi
string Mahasiswa::get_prodi() {
    return prodi;
}

// mengisi nilai prodi
void Mahasiswa::set_prodi(string prodi) {
    this->prodi = prodi;
}
// destructor
Mahasiswa::~Mahasiswa(){

}
