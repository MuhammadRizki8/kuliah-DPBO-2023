# import class
from Mahasiswa import Mahasiswa
from Tabel import Tabel

n=0#jumlah data
daftar_mahasiswa = []#array daftar mahasiswa
arrheader=["NAMA", "NIM", "Prodi", "Fakultas"]#array header
max=[0] * 4#array string terpanjang
nama=""#penampung data mahasiswa
nim=""
prodi=""
fakultas=""
for i in range(4):#tentukan string terpanjang
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
            print("Nama     : ", end="")
            nama=input()
            max[0] = max[0] if max[0] > len(nama) else len(nama)
            print("NIM      : ", end="")
            nim=input()
            max[1] = max[1] if max[1] > len(nim) else len(nim)
            print("Prodi    : ", end="")
            prodi=input()
            max[2] = max[2] if max[2] > len(prodi) else len(prodi)
            print("Fakultas : ", end="")
            fakultas=input()
            max[3] = max[3] if max[3] > len(fakultas) else len(fakultas)
            daftar_mahasiswa.append(Mahasiswa(nama, nim, prodi, fakultas))#tambahkan objek mahasiswa baru ke daftar
            print("-----------------------------")
        print(n,"data berhasil ditambahkan ke daftar\n")

    elif pil==2:
        if not daftar_mahasiswa:#jika daftar masih kosong
            print("\n=== Daftar kosong ===\n")
        else:#jika tidak
            tbl=Tabel(n, 4)#buat objek tabel
            tbl.buat_baris(arrheader, max, sum(max), '=')#tampilkan header
            for mhs in daftar_mahasiswa:
                arrisi=[ mhs.get_name(), mhs.get_nim(), mhs.get_prodi(), mhs.get_fakultas()]#isi array baris
                tbl.buat_baris(arrisi, max, sum(max), '-')#tampilkan baris

    elif pil==3:#update
        if not daftar_mahasiswa:#jika daftar kosong
            print("\n=== Daftar kosong ===\n")
        else:    
            print("Masukan NIM yang akan diupdate :")#inputkan nim data yang ingin diupdate
            nim=input()
            found=False
            for mhs in daftar_mahasiswa:#cari dalam daftar
                if mhs.get_nim() == nim:#jika ketemu
                    found=True
                    print("Nama: ", mhs.get_name())#tampilkan data awal
                    print("NIM: ", mhs.get_nim())
                    print("Program Studi: ", mhs.get_prodi())
                    print("Fakultas: ", mhs.get_fakultas())
                    print("Update Data: ")#minta inputan data baru
                    nama=input()
                    prodi=input()
                    fakultas=input()
                    max[0] = max[0] if max[0] > len(nama) else len(nama)#cek string terpanjang
                    max[2] = max[2] if max[2] > len(prodi) else len(prodi)
                    max[3] = max[3] if max[3] > len(fakultas) else len(fakultas)
                    mhs.set_name(nama)#set atribut objek
                    mhs.set_prodi(prodi)
                    mhs.set_fakultas(fakultas)
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
                if mhs.get_nim() == nim:#jika ketemu
                    found=True
                    del daftar_mahasiswa[i]#hapus objek
                    break
            if not found:#jika tidak ditemukan
                print("NIM tidak ditemukan!")

    elif pil==5:
        break

    else:
        print("Masukan pilihan yang benar!\n")
        continue

print("\n=== TERIMA KASIH ===")
