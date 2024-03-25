#include "header.hh"

// constructor kosong
Dosen::Dosen(){

}

// constructor dengan parameter
Dosen::Dosen(string nik, string nip, string nama, string jenis_kelamin, string fakultas, string pend_terakhir, string keahlian, string asal_universitas, string email_edu) : SivitasAkademik("", nama, jenis_kelamin, asal_universitas, email_edu) {
    // Menginisialisasi atribut dengan nilai parameter yang diberikan
    this->nip = nip;
    this->fakultas = fakultas;
    this->pend_terakhir=pend_terakhir;
    this->keahlian=keahlian;
}

// Mengambil nilai dari atribut nip
string Dosen::get_nip(){
    return nip;
}

// Menetapkan nilai untuk atribut nip
void Dosen::set_nip(string nip){
    this->nip = nip;
}

// Mengambil nilai dari atribut fakultas
string Dosen::get_fakultas(){
    return fakultas;
}

// Menetapkan nilai untuk atribut fakultas
void Dosen::set_fakultas(string fakultas){
    this->fakultas = fakultas;
}

// Mengambil nilai dari atribut pend_terakhir
string Dosen::get_pend_terakhir(){
    return pend_terakhir;
}

// Menetapkan nilai untuk atribut pend_terakhir
void Dosen::set_pend_terakhir(string pend_terakhir){
    this->pend_terakhir = pend_terakhir;
}

// Mengambil nilai dari atribut keahlian
string Dosen::get_keahlian(){
    return keahlian;
}

// Menetapkan nilai untuk atribut keahlian
void Dosen::set_keahlian(string keahlian){
    this->keahlian = keahlian;
}

// destructor
Dosen::~Dosen(){

}