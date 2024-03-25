// memanggil header
#include "header.hh"

// constructor kosong
Human::Human(){

}

// constructor berparameter
Human::Human(string nik, string nama, string jenis_kelamin) {
    this->nik = nik;
    this->nama = nama;
    this->jenis_kelamin = jenis_kelamin;
}

// ambil nilai nik
string Human::get_nik() {
    return nik;
}

// mengisi nilai nik
void Human::set_nik(string nik) {
    this->nik = nik;
}

// ambil nilai nama
string Human::get_nama() {
    return nama;
}

// mengisi nilai nama
void Human::set_nama(string nama) {
    this->nama = nama;
}

// ambil nilai jenis kelamin
string Human::get_jenis_kelamin() {
    return jenis_kelamin;
}

// mengisi nilai jenis kelamin
void Human::set_jenis_kelamin(string jenis_kelamin) {
    this->jenis_kelamin = jenis_kelamin;
}

// destructor
Human::~Human(){

}