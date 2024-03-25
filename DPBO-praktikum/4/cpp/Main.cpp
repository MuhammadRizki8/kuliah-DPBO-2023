#include "header.hh"

int main(){
    // membuat beberapa objek mahasiswa
    Mahasiswa mhs1 = Mahasiswa("001","2107922", "Andi", "L","Ilmu Komputer", "FPMIPA", "Universitas Pendidikan Indonesia", "andi@upi.edu");
    Mahasiswa mhs2 = Mahasiswa("002","2107923", "Budi", "L","Bahasa Indonesia" ,"FPEB", "Universitas Pendidikan Indonesia", "budi@upi.edu");
    Mahasiswa mhs3 = Mahasiswa("003","2107924", "Cici", "P", "Psikologi","FIP", "Universitas Pendidikan Indonesia", "cici@upi.edu");
    Mahasiswa mhs4 = Mahasiswa("004","2107925", "Dewi", "P","Psikologi" ,"FIP", "Universitas Pendidikan Indonesia", "dewi@upi.edu");

    // membuat beberapa objek dosen
    Dosen dsn1 = Dosen("001", "123", "Dr. Ahmad", "L", "FPMIPA", "S3", "Artificial Intelligence", "Universitas Pendidikan Indonesia", "ahmad@upi.edu");
    Dosen dsn2 = Dosen("002", "456", "Dr. Roni", "L", "FPEB", "S2", "Ekonomi Pembangunan", "Universitas Pendidikan Indonesia", "budi@upi.edu");
    Dosen dsn3 = Dosen("003", "789", "Prof. Nana", "P", "FIP", "S3", "Psikologi Klinis", "Universitas Pendidikan Indonesia", "cici@upi.edu");

    // membuat beberapa objek course
    Course course1 = Course("Pemrograman Berorientasi Objek", dsn1);
    Course course2 = Course("Ekonomi Mikro", dsn2);
    Course course3 = Course("Psikologi Anak", dsn3);

    // menambahkan mahasiswa ke dalam course
    course1.add_mahasiswa(mhs1);
    course1.add_mahasiswa(mhs2);
    course2.add_mahasiswa(mhs3);
    course3.add_mahasiswa(mhs3);
    course3.add_mahasiswa(mhs4);

    // membuat beberapa objek program studi
    ProgramStudi prodi1 = ProgramStudi("Ilmu Komputer", "ILK");
    ProgramStudi prodi2 = ProgramStudi("Ekonomi", "EKO");
    ProgramStudi prodi3 = ProgramStudi("Psikologi", "PSI");

    // menambahkan course ke dalam program studi
    prodi1.add_course(course1);
    prodi2.add_course(course2);
    prodi3.add_course(course3);

    // membuat vector berisi objek
    vector<Mahasiswa> mahasiswa_list={mhs1, mhs2, mhs3, mhs4};
    vector<Dosen> dosens = {dsn1, dsn2, dsn3};
    vector<Course> courses ={course1, course2, course3};
    vector<ProgramStudi> prodi_list={prodi1, prodi2, prodi3};

    cout << "=======================================" << endl;
    // menampilkan data mahasiswa
    cout << "Daftar Mahasiswa:" << endl;
    for (Mahasiswa mhs : mahasiswa_list) {
    cout << "---------------------------------------" << endl;
    cout << "NIM         : " << mhs.get_nim() << endl;
    cout << "Nama        : " << mhs.get_nama() << endl;
    cout << "Prodi       : " << mhs.get_prodi()<<endl;
    cout << "Fakultas    : " << mhs.get_fakultas() << endl;
    cout << "Universitas : " << mhs.get_asal_universitas() << endl;
    }
    cout << "=======================================" << endl;


    // menampilkan data dosen
    cout << "\n=======================================\n";
    cout << "Daftar Dosen:\n";
    for (Dosen dsn : dosens) {
        cout << "---------------------------------------\n";
        cout << "NIP                 : " << dsn.get_nip() << endl;
        cout << "Nama                : " << dsn.get_nama() << endl;
        cout << "Jenis Kelamin       : " << dsn.get_jenis_kelamin() << endl;
        cout << "Fakultas            : " << dsn.get_fakultas() << endl;
        cout << "Pendidikan Terakhir : " << dsn.get_pend_terakhir() << endl;
        cout << "Keahlian            : " << dsn.get_keahlian() << endl;
    }
    cout << "=======================================\n";

    // menampilkan data course
    cout << "\n=======================================\n";
    cout << "Daftar Course:\n";
    for (Course course : courses ) {
        cout << "---------------------------------------\n";
        cout << "Nama              : " << course.get_nama_matakuliah() << endl;
        cout << "Dosen Pengampu    : " << course.get_dosen().get_nama() << endl;
        cout << "Daftar Mahasiswa  :\n";
        // tampilkan list mahasiswanya
        for (auto mhs : course.get_mahasiswa()) {
            cout << "                   -> " << mhs.get_nama() << endl;
        }
    }
    cout << "=======================================\n";


    // menampilkan data program studi
    cout << "\n=======================================\n";
    cout << "Daftar Program Studi:\n";
    for (auto prodi : prodi_list) {
        cout << "---------------------------------------\n";
        cout << "Nama          : " << prodi.get_nama_prodi() << endl;
        cout << "Kode          : " << prodi.get_kode() << endl;
        cout << "Daftar Course :\n";
        // tampilkan list course nya
        for (auto course : prodi.get_courses()) {
            cout << "               -> " << course.get_nama_matakuliah() << endl;
            cout << "                  Daftar Mahasiswa :\n";
            // tampilkan list mahasiswanya
            for (auto mhs : course.get_mahasiswa()) {
                cout << "                                    --> " << mhs.get_nama() << endl;
            }
        }
    }
    cout << "=======================================\n";

    return 0;
}