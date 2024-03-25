# import class
from Mahasiswa import Mahasiswa
from Tabel import Tabel

n=0#jumlah data
daftar_mahasiswa = []#array daftar mahasiswa
arrheader=["NIK", "Nama", "Gender", "Universitas", "Email", "NIM", "Fakultas", "Program Studi"]#array header
arrisi=[""]*8
max=[0] * 8#array string terpanjang
nama=""#penampung data mahasiswa
nim=""
prodi=""
fakultas=""
for i in range(8):#tentukan string terpanjang
    max[i]=max[i] if max[i]>len(arrheader[i]) else len(arrheader[i])

while True:
    print("1. Tambah Data")
    print("2. Tampilkan Daftar")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar")
    print("-----------------------------")
    pil=int(input("Masukan Pilihan(1-5) :"))#inputkan pilihan

    if pil==1:
        n=int(input("\nMasukan banyak Mahasiswa :"))#inputkan jumlah data
        for i in range(n):
            print("Masukan data mahasiswa ke",i+1)#masukan data lalu cek string sterpanjangnya
            for j in range(8):
                print(arrheader[j]+ " : ", end="")
                arrisi[j]=input()
                max[j] = max[j] if max[j] > len(arrisi[j]) else len(arrisi[j])
            daftar_mahasiswa.append(Mahasiswa(arrisi[0], arrisi[1], arrisi[2], arrisi[3], arrisi[4], arrisi[5], arrisi[6], arrisi[7]))#tambahkan objek mahasiswa baru ke daftar
            print("-----------------------------")
        print(n,"data berhasil ditambahkan ke daftar\n")

    elif pil==2:
        if not daftar_mahasiswa:#jika daftar masih kosong
            print("\n=== Daftar kosong ===\n")
        else:#jika tidak
            tbl=Tabel(n, 8)#buat objek tabel
            tbl.buat_baris(arrheader, max, sum(max), '=')#tampilkan header
            for mhs in daftar_mahasiswa:
                arrisi=[mhs.getNIK() ,mhs.getNama(), mhs.getGender(), mhs.getUniversitas(), mhs.getEmail(),mhs.getNIM(), mhs.getFakultas(), mhs.getStudiProgram() ]#isi array baris
                tbl.buat_baris(arrisi, max, sum(max), '-')#tampilkan baris

    elif pil==3:#update
        if not daftar_mahasiswa:#jika daftar kosong
            print("\n=== Daftar kosong ===\n")
        else:    
            print("Masukan NIM yang akan diupdate :")#inputkan nim data yang ingin diupdate
            nim=input()
            found=False
            for mhs in daftar_mahasiswa:#cari dalam daftar
                if mhs.getNIM() == nim:#jika ketemu
                    found=True
                    arrisi=[mhs.getNIK() ,mhs.getNama(), mhs.getGender(), mhs.getUniversitas(), mhs.getEmail(),mhs.getNIM(), mhs.getFakultas(), mhs.getStudiProgram() ]#isi array baris
                    tbl.buat_baris(arrisi, max, sum(max), '-')#tampilkan baris
                    print("Update Data: ")#minta inputan data baru
                    for j in range(8):
                        if j==5:
                            continue
                        print(arrheader[j]+ " : ", end="")
                        arrisi[j]=input()
                        max[j] = max[j] if max[j] > len(arrisi[j]) else len(arrisi[j])
                    # "NIK", "Nama", "Gender", "Universitas", "Email", "NIM", "Fakultas", "Program Studi"
                    mhs.setNIK(arrisi[0])
                    mhs.setNama(arrisi[1])
                    mhs.setGender(arrisi[2])
                    mhs.setUniversitas(arrisi[3])
                    mhs.setEmail(arrisi[4])
                    mhs.setFakultas(arrisi[6])
                    mhs.setStudiProgram(arrisi[7])
                    print("Data berhasil diupdate\n")
            if not found:#jika tidak ditemukan
                print("NIM tidak ditemukan!")

    elif pil==4:#delete
        if not daftar_mahasiswa:#jika daftar kosong
            print("\n=== Daftar kosong ===\n")
        else:   
            print("Masukan NIM yang akan dihapus :")#masukan nim data yang ingin dihapus
            nim=input()
            found=False
            for i, mhs in enumerate(daftar_mahasiswa):#cari dalam daftar
                if mhs.getNIM() == nim:#jika ketemu
                    found=True
                    del daftar_mahasiswa[i]#hapus objek
                    print("Data berhasil dihapus\n")
                    break
            if not found:#jika tidak ditemukan
                print("NIM tidak ditemukan!")

    elif pil==5:
        break

    else:
        print("Masukan pilihan yang benar!\n")
        continue

print("\n=== TERIMA KASIH ===")
