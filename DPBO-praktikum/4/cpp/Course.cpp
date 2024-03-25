#include "header.hh"

// konstruktor kelas Course
Course::Course(string nama_matakuliah, Dosen dosen) {
    this->nama_matakuliah = nama_matakuliah;
    this->dosen = dosen;
}

// destruktor kelas Course
Course::~Course() {
    mahasiswa.clear(); // Menghapus semua elemen pada vektor mahasiswa
}

// fungsi getter untuk mengembalikan nilai atribut nama_matakuliah
string Course::get_nama_matakuliah() {
    return this->nama_matakuliah;
}

// fungsi setter untuk mengubah nilai atribut nama_matakuliah
void Course::set_nama_matakuliah(string nama_matakuliah) {
    this->nama_matakuliah = nama_matakuliah;
}

// fungsi getter untuk mengembalikan nilai atribut dosen
Dosen Course::get_dosen() {
    return this->dosen;
}

// fungsi setter untuk mengubah nilai atribut dosen
void Course::set_dosen(Dosen dosen) {
    this->dosen = dosen;
}

// fungsi getter untuk mengembalikan vektor mahasiswa
vector<Mahasiswa> Course::get_mahasiswa() {
    return this->mahasiswa;
}

// fungsi untuk menambahkan objek mahasiswa ke vektor mahasiswa
void Course::add_mahasiswa(Mahasiswa mahasiswa) {
    this->mahasiswa.push_back(mahasiswa);
}
