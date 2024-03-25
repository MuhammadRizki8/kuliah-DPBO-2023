from Classes import *

alamat_pemilik = Alamat("Jl. Merdeka", "Kel. Cipaganti", "Kec. Coblong", "Kota Bandung", "Jawa Barat")
pemilik = PemilikKios("P001", ["K001", "K002"], "1234567890", "John Doe", alamat_pemilik)

alamat_karyawan_pengelola = Alamat("Jl. Sudirman", "Kel. Dago", "Kec. Coblong", "Kota Bandung", "Jawa Barat")
karyawan_pengelola = KaryawanPengelola("KP001", "0987654321", "Jane Doe", alamat_karyawan_pengelola, "Minggu")

alamat_karyawan_kios = Alamat("Jl. Asia Afrika", "Kel. Braga", "Kec. Sumur Bandung", "Kota Bandung", "Jawa Barat")
karyawan_kios = KaryawanKios("KK001", "1357924680", "Bob Smith", alamat_karyawan_kios, "Senin")

print("Data Pemilik Kios")
print("Nama Pemilik Kios :", pemilik.getNama())
print("Alamat Pemilik Kios :", pemilik.getAlamat().getJalan(), pemilik.getAlamat().getDesaKelurahan(), pemilik.getAlamat().getKecamatan(), pemilik.getAlamat().getKabupatenKota(), pemilik.getAlamat().getProvinsi())
print("Kode Kios yang dimiliki :", pemilik.getKodeKiosList())
pemilik.tambah_kode_kios("K003")
print("Kode Kios setelah ditambahkan :", pemilik.getKodeKiosList())

print("\nData Karyawan Pengelola")
print("Nama Karyawan Pengelola :", karyawan_pengelola.getNama())
print("Alamat Karyawan Pengelola :", karyawan_pengelola.getAlamat().getJalan(), karyawan_pengelola.getAlamat().getDesaKelurahan(), karyawan_pengelola.getAlamat().getKecamatan(), karyawan_pengelola.getAlamat().getKabupatenKota(), karyawan_pengelola.getAlamat().getProvinsi())
print("Hari Libur Karyawan Pengelola :", karyawan_pengelola.getLiburShift())

print("\nData Karyawan Kios")
print("Nama Karyawan Kios :", karyawan_kios.getNama())
print("Alamat Karyawan Kios :", karyawan_kios.getAlamat().getJalan(), karyawan_kios.getAlamat().getDesaKelurahan(), karyawan_kios.getAlamat().getKecamatan(), karyawan_kios.getAlamat().getKabupatenKota(), karyawan_kios.getAlamat().getProvinsi())
print("Hari Libur Karyawan Kios :", karyawan_kios.getLiburShift())