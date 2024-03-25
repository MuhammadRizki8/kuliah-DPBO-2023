from Main import *
# membuat objek transaksi
transaksi1 = Transaksi("K001", "2023-03-01", "KK001", "KP001")
transaksi1.tambah_makanan("M001")
transaksi1.tambah_minuman("MN001")

transaksi2 = Transaksi("K002", "2023-03-01", "KK001", "KP001")
transaksi2.tambah_makanan("M002")
transaksi2.tambah_minuman("MN002")

transaksi3 = Transaksi("K003", "2023-03-01", "KK002", "KP002")
transaksi3.tambah_makanan("M003")
transaksi3.tambah_minuman("MN003")

transaksi4 = Transaksi("K004", "2023-03-01", "KK002", "KP002")
transaksi4.tambah_makanan("M004")
transaksi4.tambah_minuman("MN004")

transaksi5 = Transaksi("K005", "2023-03-01", "KK001", "KP001")
transaksi5.tambah_makanan("M005")
transaksi5.tambah_minuman("MN005")

transaksi6 = Transaksi("K006", "2023-03-01", "KK002", "KP002")
transaksi6.tambah_makanan("M006")
transaksi6.tambah_minuman("MN006")

# menampilkan daftar transaksi
daftar_transaksi = [transaksi1, transaksi2, transaksi3, transaksi4, transaksi5, transaksi6]

for i, transaksi in enumerate(daftar_transaksi):
    print(f"Transaksi {i+1}")
    print(f"Kode Kios: {transaksi.get_kode_kios()}")
    print(f"Tanggal: {transaksi.get_tanggal()}")
    print(f"Kode Makanan: {transaksi.kodeMakanan}")
    print(f"Kode Minuman: {transaksi.kodeMinuman}")
    print(f"Kode Karyawan Kios: {transaksi.get_kode_karyawan_kios()}")
    print(f"Kode Karyawan Pengelola: {transaksi.get_kode_karyawan_pengelola()}")
    print()


pembagian1 = PembagianTransaksiPerHari("K001", 0, 0, "2022-03-01", "Pemilik 1", [transaksi1])
pembagian2 = PembagianTransaksiPerHari("K002", 0, 0, "2022-03-01", "Pemilik 2", [transaksi2])
