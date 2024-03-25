// memanggil file header
#include "header.hh"

// constructor kosong
ProgramStudi::ProgramStudi(){

}

// constructor berparameter
ProgramStudi::ProgramStudi(string nama_prodi, string kode) : nama_prodi(nama_prodi), kode(kode) {

}

// ambil nilai nama prodi
string ProgramStudi::get_nama_prodi() {
    return nama_prodi;
}

// mengisi nilai nama prodi
void ProgramStudi::set_nama_prodi(string nama_prodi) {
    this->nama_prodi = nama_prodi;
}

// ambil nilai kode
string ProgramStudi::get_kode() {
    return kode;
}

// mengisi nilai kode
void ProgramStudi::set_kode(string kode) {
    this->kode = kode;
}

// ambil nilai course
vector<Course> ProgramStudi::get_courses() {
    return courses;
}

// menambahkkan course
void ProgramStudi::add_course(Course course) { // bukan pointer
    courses.push_back(course);
}

// destructor
ProgramStudi::~ProgramStudi() { // tidak perlu dealokasi karena tidak menggunakan pointer
}
