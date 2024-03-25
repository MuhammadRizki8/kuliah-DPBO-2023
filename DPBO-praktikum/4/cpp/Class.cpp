// #include <iostream>
// #include<vector>
// #include<string>
// using namespace std;

// class Human {
//     private:
//     string nik;
//     string nama;
//     string jenis_kelamin;

//     public:
//     Human(){

//     }

//     Human(string nik, string nama, string jenis_kelamin) {
//     this->nik = nik;
//     this->nama = nama;
//     this->jenis_kelamin = jenis_kelamin;
//     }
//     string get_nik() {
//         return nik;
//     }

//     void set_nik(string nik) {
//         this->nik = nik;
//     }

//     string get_nama() {
//         return nama;
//     }

//     void set_nama(string nama) {
//         this->nama = nama;
//     }

//     string get_jenis_kelamin() {
//         return jenis_kelamin;
//     }

//     void set_jenis_kelamin(string jenis_kelamin) {
//         this->jenis_kelamin = jenis_kelamin;
//     }

//     ~Human(){

//     }
// };

// class SivitasAkademik : public Human {
//     private:
//     string asal_universitas;
//     string email_edu;

//     public:
//     SivitasAkademik(){

//     }

//     SivitasAkademik(string nik, string nama, string jenis_kelamin, string asal_universitas, string email_edu)
//     : Human(nik, nama, jenis_kelamin) {
//     this->asal_universitas = asal_universitas;
//     this->email_edu = email_edu;
//     }
//     void set_asal_universitas(string asal_universitas) {
//         this->asal_universitas = asal_universitas;
//     }

//     string get_asal_universitas() {
//         return asal_universitas;
//     }

//     void set_email_edu(string email_edu) {
//         this->email_edu = email_edu;
//     }

//     string get_email_edu() {
//         return email_edu;
//     }
//     ~SivitasAkademik(){

//     }
// };

// class Mahasiswa : public SivitasAkademik {
//     private:
//     string nim;
//     string fakultas;
//     string prodi;

//     public:
//     Mahasiswa(string nik,string nim, string nama, string jenis_kelamin, string fakultas, string asal_universitas, string email_edu)
//     : SivitasAkademik(nik, nama, jenis_kelamin, asal_universitas, email_edu) {
//     this->nim = nim;
//     this->fakultas = fakultas;
//     this->prodi = "";
//     }
//     string get_nim() {
//         return nim;
//     }

//     void set_nim(string nim) {
//         this->nim = nim;
//     }

//     string get_fakultas() {
//         return fakultas;
//     }

//     void set_fakultas(string fakultas) {
//         this->fakultas = fakultas;
//     }

//     string get_prodi() {
//         return prodi;
//     }

//     void set_prodi(string prodi) {
//         this->prodi = prodi;
//     }
//     ~Mahasiswa(){

//     }
// };

// class Dosen : public SivitasAkademik {
//     private:
//         string nip;
//         string fakultas;
//         string pend_terakhir;
//         string keahlian;
//     public:
//         Dosen(){
            
//         }

//         Dosen(string nik, string nip, string nama, string jenis_kelamin, string fakultas, string pend_terakhir, string keahlian, string asal_universitas, string email_edu) : SivitasAkademik("", nama, jenis_kelamin, asal_universitas, email_edu) {
//             this->nip = nip;
//             this->fakultas = fakultas;
//             this->pend_terakhir=pend_terakhir;
//             this->keahlian=keahlian;
//         };
        
//         string get_nip(){
//             return nip;
//         };
//         void set_nip(string nip){
//             this->nip = nip;
//         };

//         string get_fakultas(){
//             return fakultas;
//         };
//         void set_fakultas(string fakultas){
//             this->fakultas = fakultas;
//         };

//         string get_pend_terakhir(){
//             return pend_terakhir;
//         };
//         void set_pend_terakhir(string pend_terakhir){
//             this->pend_terakhir = pend_terakhir;
//         };
//         string get_keahlian(){
//             return keahlian;
//         };
//         void set_keahlian(string keahlian){
//             this->keahlian = keahlian;
//         };
// };

// class Course {
//     private:
//         string nama_matakuliah;
//         Dosen dosen;
//         vector<Mahasiswa> mahasiswa;

//     public:
//         Course(string nama_matakuliah, Dosen dosen) {
//             this->nama_matakuliah = nama_matakuliah;
//             this->dosen = dosen;
//         }

//         ~Course() {
//             mahasiswa.clear();
//         }

//         string get_nama_matakuliah() {
//             return this->nama_matakuliah;
//         }

//         void set_nama_matakuliah(string nama_matakuliah) {
//             this->nama_matakuliah = nama_matakuliah;
//         }

//         Dosen get_dosen() {
//             return this->dosen;
//         }

//         void set_dosen(Dosen dosen) {
//             this->dosen = dosen;
//         }

//         vector<Mahasiswa> get_mahasiswa() {
//             return this->mahasiswa;
//         }

//         void add_mahasiswa(Mahasiswa mahasiswa) {
//             this->mahasiswa.push_back(mahasiswa);
//         }
// };


// class ProgramStudi {
// private:
//     string nama_prodi;
//     string kode;
//     vector<Course> courses; // tidak menggunakan pointer
// public:
//     ProgramStudi(string nama_prodi, string kode) : nama_prodi(nama_prodi), kode(kode) {}

//     string get_nama_prodi() {
//         return nama_prodi;
//     }

//     void set_nama_prodi(string nama_prodi) {
//         this->nama_prodi = nama_prodi;
//     }

//     string get_kode() {
//         return kode;
//     }

//     void set_kode(string kode) {
//         this->kode = kode;
//     }

//     vector<Course> get_courses() {
//         return courses;
//     }

//     void add_course(Course course) { // bukan pointer
//         courses.push_back(course);
//     }

//     ~ProgramStudi() { // tidak perlu dealokasi karena tidak menggunakan pointer
//     }
// };
