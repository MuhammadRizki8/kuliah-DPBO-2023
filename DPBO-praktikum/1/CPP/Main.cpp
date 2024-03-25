//memanggil class mahasiswa dan tabel
#include "Mahasiswa.cpp"
#include "Tabel.cpp"

int main(){
    int pil, n;//var pilihan dan jumlah input data mahasiswa
    list<Mahasiswa> daftar_Mahasiswa;//list daftar
    array<string, 4> arrheader = {"Nama", "NIM", "Prodi", "Fakultas"};//array header tabel
    array<string, 4> arrisi = { };//array isi tabel
    int max[4] = {};//array string terpanjang
    for(int i=0; i<4; i++)
        max[i] = (max[i] > arrheader[i].length()) ? max[i] : arrheader[i].length();//simpan nilai string terpanjang
    do{
        cout<<"1. Tambah Data"<<endl;
        cout<<"2. Tampilkan Daftar"<<endl;
        cout<<"3. Update Data"<<endl;
        cout<<"4. Hapus Data"<<endl;
        cout<<"5. Keluar"<<endl;
        cout<<"-----------------------------"<<endl; 
        cout<<"Masukan Pilihan(1-5) : ";cin>>pil;//inputan pilihan
        cin.ignore();//bersihkan buffer input
        switch (pil){
        case 1://tambah mahasiswa
            cout<<"\nMasukan banyak Mahasiswa : ";cin>>n;//masukan jmlh mahasiswa
            cin.ignore();//bersihkan buffer input
            for(int i=0; i<n; i++){
                cout<<"Masukan data mahasiswa ke"<<i+1<<endl;//isi data mahasiswa
                cout<<"Masukan Nama          : ";
                getline(cin, arrisi[0]);
                cout<<"Masukan NIM           : ";
                getline(cin, arrisi[1]);
                cout<<"Masukan Program Studi : ";
                getline(cin, arrisi[2]);
                cout<<"Masukan Fakultas      : ";
                getline(cin, arrisi[3]);
                for(int i=0; i<4; i++)
                    max[i] = (max[i] > arrisi[i].length()) ? max[i] : arrisi[i].length();//simpan nilai string terpanjang
                daftar_Mahasiswa.push_back(Mahasiswa(arrisi[0], arrisi[1],arrisi[2],arrisi[3]));//tambahkan ke list daftar mahasiswa
                cout<<"-----------------------------"<<endl;
            }
            cout<<n<<" data berhasil ditambahkan ke daftar"<<endl<<endl;
            break;
        case 2://update data
            cout<<"-------------------------------"<<endl;
            if (daftar_Mahasiswa.empty()) {//jika daftar masih kosong
                cout << "\n=== Daftar kosong ===\n" << endl;
            } else {//jika tidak
                Tabel tbl(daftar_Mahasiswa.size(), 4);//buat objek tabel dengan 4 kolom dan baris sebanyak isi list
                tbl.buat_baris(arrheader, max, max[0] + max[1] + max[2] + max[3], '=');//buat baris header
                for (Mahasiswa mhs : daftar_Mahasiswa) {
                    arrisi = { mhs.get_name(), mhs.get_nim(), mhs.get_prodi(), mhs.get_fakultas() };//mengisi array
                    tbl.buat_baris(arrisi, max, max[0] + max[1] + max[2] + max[3], '-');//buat baris isi
                }
            }
            cout<<endl;
            break;
        case 3://update
            cout<<"-------------------------------"<<endl;
            if (daftar_Mahasiswa.empty()) {
                cout << "\n=== Daftar kosong ===\n" << endl;
            } else {
                cout << "\nMasukkan NIM mahasiswa yang akan diupdate: ";
                getline(cin, arrisi[1]);//meminta inputan nim
                for (list<Mahasiswa>::iterator it = daftar_Mahasiswa.begin(); it != daftar_Mahasiswa.end(); it++) {//loop mencari nim
                    if (it->get_nim() == arrisi[1]) {//jika ketemu, maka masukan data baru
                        cout << "Masukkan Nama          : ";
                        getline(cin, arrisi[0]);
                        cout << "Masukkan Program Studi : ";
                        getline(cin, arrisi[2]);
                        cout << "Masukkan Fakultas      : ";
                        getline(cin, arrisi[3]);
                        for(int i=0; i<4; i++)
                            max[i] = (max[i] > arrisi[i].length()) ? max[i] : arrisi[i].length();//cek kembali string terpanjangnya
                        it->set_name(arrisi[0]);//ubah atribut dengan set
                        it->set_prodi(arrisi[2]);
                        it->set_fakultas(arrisi[3]);
                        cout << "\nData mahasiswa berhasil diupdate\n" << endl;
                        break;
                    }
                }
            }
            break;
        case 4://delete
            cout<<"-------------------------------"<<endl;
            if (daftar_Mahasiswa.empty()) {//jika daftar kosong
                cout << "\n=== Daftar kosong ===\n" << endl;
            } else {
                cout << "\nMasukkan NIM mahasiswa yang akan dihapus: ";
                getline(cin, arrisi[1]);//masukan nim
                for (list<Mahasiswa>::iterator it = daftar_Mahasiswa.begin(); it != daftar_Mahasiswa.end(); it++) {//cari nim
                    if (it->get_nim() == arrisi[1]) {//jika ketemu
                        daftar_Mahasiswa.erase(it);//hapus dari daftar
                        cout << "\nData mahasiswa berhasil dihapus\n" << endl;
                        break;
                    }
                }
            }
            break;
        case 5://out
            break;    
        default:
            cout<<"-------------------------------"<<endl;
            cout << "\n=== Masukan Input dengan Benar! ===\n" << endl;
            break;
        }
    }while(pil!=5);
    cout<<"\n=== TERIMA KASIH ==="<<endl;
}
