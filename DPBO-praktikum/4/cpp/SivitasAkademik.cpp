// memanggil file header
#include "header.hh"

// constructor kosong
SivitasAkademik::SivitasAkademik(){

}

// constructor berparameter
SivitasAkademik::SivitasAkademik(string nik, string nama, string jenis_kelamin, string asal_universitas, string email_edu)
: Human(nik, nama, jenis_kelamin) {
    this->asal_universitas = asal_universitas;
    this->email_edu = email_edu;
}

// mengisi nilai asal universitas
void SivitasAkademik::set_asal_universitas(string asal_universitas) {
    this->asal_universitas = asal_universitas;
}

// mengambil nilai universitas
string SivitasAkademik::get_asal_universitas() {
    return asal_universitas;
}

// mengisi nilai email
void SivitasAkademik::set_email_edu(string email_edu) {
    this->email_edu = email_edu;
}

// mengambil nilai email
string SivitasAkademik::get_email_edu() {
    return email_edu;
}

// destructor
SivitasAkademik::~SivitasAkademik(){

}
