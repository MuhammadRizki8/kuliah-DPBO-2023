#include "Mahasiswa.cpp"
#include "Tabel.cpp"
#include <vector>
#include <array>

int main(){
    int n = 0;
    vector<Mahasiswa> daftarMahasiswa;
    string arrisi[8];
    string arrheader[]={"NIK", "NAMA", "GENDER", "UNIVERSITAS", "EMAIL", "NIM", "FAKULTAS", "PROGRAM STUDI"};//array untuk header tabel
    int max[8] = { (int)arrheader[0].length(), (int)arrheader[1].length(), (int)arrheader[2].length(), (int)arrheader[3].length(), (int)arrheader[4].length(), (int)arrheader[5].length(), (int)arrheader[6].length(), (int)arrheader[7].length() };
    cout << "Masukan banyak Mahasiswa :" << endl;
    // input jumlah mahasiswa
    try {
        cin >> n;
    }
    catch (exception e) {
        cout << "Inputan harus berupa angka!" << endl;
    }

    cin.ignore(); // membersihkan buffer input
    for (int i = 0; i < n; i++) {
        cout << "\n-----------------------------" << endl;
        cout << "Masukan data mahasiswa ke-" << (i + 1) << " :" << endl; // input data mahasiswa
        for (int j = 0; j < 8; j++) {
            getline(cin, arrisi[j]);
            max[j] = max[j] > arrisi[j].length() ? max[j] : arrisi[j].length(); // cek nilai string terpanjang
        }
        Mahasiswa mahasiswa1 = Mahasiswa(arrisi[0], arrisi[1], arrisi[2], arrisi[3], arrisi[4], arrisi[5], arrisi[6], arrisi[7]); // buat objek
        daftarMahasiswa.push_back(mahasiswa1); // tambahkan objek ke list daftar
    }

        int sum = 0;
        for (int i = 0; i < 8 ; i++) {
            sum += max[i];
        }//jumlahkan isi array max
        cout<<"\n-----------------------------"<<endl;
        cout<<"Daftar Mahasiswa : "<<endl;

        Tabel tab=Tabel(n, 8);//buat objek tabel
        tab.buat_baris(arrheader, max, sum, '=');//tampilkan tabel header
        for (int i = 0; i < daftarMahasiswa.size(); i++) {//loopdata per-mahasiswa 
            arrisi[0]=daftarMahasiswa[i].getNIK();
            arrisi[1]=daftarMahasiswa[i].getnama();
            arrisi[2]=daftarMahasiswa[i].getGender();
            arrisi[3]=daftarMahasiswa[i].getUniversitas();
            arrisi[4]=daftarMahasiswa[i].getEmail();
            arrisi[5]=daftarMahasiswa[i].getNIM();
            arrisi[6]=daftarMahasiswa[i].getFakultas();
            arrisi[7]=daftarMahasiswa[i].getStudiProgram();
            tab.buat_baris(arrisi, max, sum, '-');//
        }


    return 0;
}