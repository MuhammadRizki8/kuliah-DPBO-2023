from Classes import *

# Membuat objek pertama
transaksi1 = Transaksi("K001", "2022-03-01", ["M001", "M002", "M003"], ["MI001"])
transaksi1.tambah_minuman("MN001")
transaksi1.tambah_minuman("MN002")
transaksi1.tambah_minuman("MN003")
transaksi1.tambah_minuman("MN004")

pembagian1 = PembagianTransaksiPerHari("K001", 0, 0, "2022-03-01", "Pemilik 1", [transaksi1])

# Membuat objek kedua
transaksi2 = Transaksi("K002", "2022-03-01", ["M004", "M005", "M006"], ["MI002"])
transaksi2.tambah_minuman("MN005")
transaksi2.tambah_minuman("MN006")

pembagian2 = PembagianTransaksiPerHari("K002", 0, 0, "2022-03-01", "Pemilik 2", [transaksi2])

# Membuat objek ketiga
transaksi3 = Transaksi("K003", "2022-03-02", ["M007", "M008", "M009"], ["MI003"])
transaksi3.tambah_minuman("MN007")
transaksi3.tambah_minuman("MN008")

pembagian3 = PembagianTransaksiPerHari("K003", 0, 0, "2022-03-02", "Pemilik 3", [transaksi3])

# Membuat objek keempat
transaksi4 = Transaksi("K001", "2022-03-02", ["M010", "M011", "M012"], ["MI001"])
transaksi4.tambah_minuman("MN001")
transaksi4.tambah_minuman("MN002")
transaksi4.tambah_minuman("MN003")
transaksi4.tambah_minuman("MN004")
transaksi4.tambah_minuman("MN005")

pembagian4 = PembagianTransaksiPerHari("K001", 0, 0, "2022-03-02", "Pemilik 1", [transaksi4])

pembagian_list = [pembagian1, pembagian2, pembagian3, pembagian4]

for pembagian in pembagian_list:
    print("Kode Kios: {}".format(pembagian.get_kode_kios()))
    print("Omset Dibagikan: {}".format(pembagian.get_omset_dibagikan()))
    print("Bagian Pengelola: {}".format(pembagian.get_bagian_pengelola()))
    print("Tanggal: {}".format(pembagian.get_tanggal()))
    print("Pemilik: {}".format(pembagian.get_pemilik()))
    print("Transaksi: ")
    
    for transaksi in pembagian.get_transaksi():
        print("\tKode Makanan: {}".format(transaksi.get_kode_makanan()))
        print("\tKode Minuman: {}".format(transaksi.get_kode_minuman()))
        print("\tKode Karyawan Kios: {}".
