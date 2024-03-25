// Inisialisasi header file yang digunakan

#include <iostream>
#include<vector>
#include<string>
using namespace std;

// Deklarasi kelas Human
class Human {
    private:
        string nik;
        string nama;
        string jenis_kelamin;
    public:
        Human();
        Human(string nik, string nama, string jenis_kelamin);
        string get_nik();
        void set_nik(string nik);
        string get_nama();
        void set_nama(string nama);
        string get_jenis_kelamin();
        void set_jenis_kelamin(string jenis_kelamin);
        ~Human();
};

// Deklarasi kelas SivitasAkademik yang mewarisi kelas Human
class SivitasAkademik : public Human {
    private:
        string asal_universitas;
        string email_edu;
    public:
        SivitasAkademik();
        SivitasAkademik(string nik, string nama, string jenis_kelamin, string asal_universitas, string email_edu);
        void set_asal_universitas(string asal_universitas);
        string get_asal_universitas();
        void set_email_edu(string email_edu);
        string get_email_edu();
        ~SivitasAkademik();
};

// Deklarasi kelas Mahasiswa yang mewarisi kelas SivitasAkademik
class Mahasiswa : public SivitasAkademik {
    private:
        string nim;
        string fakultas;
        string prodi;
    public:
        Mahasiswa();
        Mahasiswa(string nik,string nim, string nama, string jenis_kelamin, string prodi,string fakultas, string asal_universitas, string email_edu);
        string get_nim();
        void set_nim(string nim);
        string get_fakultas();
        void set_fakultas(string fakultas);
        string get_prodi();
        void set_prodi(string prodi);
        ~Mahasiswa();
};

// Deklarasi kelas Dosen yang mewarisi kelas SivitasAkademik
class Dosen : public SivitasAkademik {
    private:
        string nip;
        string fakultas;
        string pend_terakhir;
        string keahlian;
    public:
        Dosen();
        Dosen(string nik, string nip, string nama, string jenis_kelamin, string fakultas, string pend_terakhir, string keahlian, string asal_universitas, string email_edu);
        string get_nip();
        void set_nip(string nip);
        string get_fakultas();
        void set_fakultas(string fakultas);
        string get_pend_terakhir();
        void set_pend_terakhir(string pend_terakhir);
        string get_keahlian();
        void set_keahlian(string keahlian);
        ~Dosen();
};

// Deklarasi kelas Course
class Course {
    private:
        string nama_matakuliah;
        Dosen dosen;
        vector<Mahasiswa> mahasiswa;
    public:
        Course();
        Course(string nama_matakuliah, Dosen dosen);
        string get_nama_matakuliah();
        void set_nama_matakuliah(string nama_matakuliah);
        Dosen get_dosen();
        void set_dosen(Dosen dosen) ;
        vector<Mahasiswa> get_mahasiswa();
        void add_mahasiswa(Mahasiswa mahasiswa);
        ~Course();
};

// deklarasi kelas program studi
class ProgramStudi {
private:
    string nama_prodi;
    string kode;
    vector<Course> courses; // tidak menggunakan pointer
public:
    ProgramStudi();
    ProgramStudi(string nama_prodi, string kode);
    string get_nama_prodi();
    void set_nama_prodi(string nama_prodi);
    string get_kode();
    void set_kode(string kode);
    vector<Course> get_courses() ;
    void add_course(Course course) ;
    ~ProgramStudi();
};
