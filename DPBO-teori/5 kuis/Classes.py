class Human:
    def __init__(self, NoKTP, nama, alamat):
        self.__NoKTP = NoKTP
        self.__nama = nama
        self.__alamat = alamat
    
    def getNoKTP(self):
        return self.__NoKTP
    
    def setNoKTP(self, NoKTP):
        self.__NoKTP = NoKTP
    
    def getNama(self):
        return self.__nama
    
    def setNama(self, nama):
        self.__nama = nama
    
    def getAlamat(self):
        return self.__alamat
    
    def setAlamat(self, alamat):
        self.__alamat = alamat


class Alamat:
    def __init__(self, jalan, desaKelurahan, kecamatan, kabupatenKota, provinsi, negara=None):
        self.__jalan = jalan
        self.__desaKelurahan = desaKelurahan
        self.__kecamatan = kecamatan
        self.__kabupatenKota = kabupatenKota
        self.__provinsi = provinsi
        self.__negara = negara
    
    def getJalan(self):
        return self.__jalan
    
    def setJalan(self, jalan):
        self.__jalan = jalan
    
    def getDesaKelurahan(self):
        return self.__desaKelurahan
    
    def setDesaKelurahan(self, desaKelurahan):
        self.__desaKelurahan = desaKelurahan
    
    def getKecamatan(self):
        return self.__kecamatan
    
    def setKecamatan(self, kecamatan):
        self.__kecamatan = kecamatan
    
    def getKabupatenKota(self):
        return self.__kabupatenKota
    
    def setKabupatenKota(self, kabupatenKota):
        self.__kabupatenKota = kabupatenKota
    
    def getProvinsi(self):
        return self.__provinsi
    
    def setProvinsi(self, provinsi):
        self.__provinsi = provinsi
    
    def getNegara(self):
        return self.__negara
    
    def setNegara(self, negara):
        self.__negara = negara


class PemilikKios(Human):
    def __init__(self, kodePemilikKios, kodeKiosList, NoKTP, nama, alamat):
        super().__init__(NoKTP, nama, alamat)
        self.__kodePemilikKios = kodePemilikKios
        self.__kodeKiosList = kodeKiosList
    
    def getKodePemilikKios(self):
        return self.__kodePemilikKios
    
    def setKodePemilikKios(self, kodePemilikKios):
        self.__kodePemilikKios = kodePemilikKios
    
    def getKodeKiosList(self):
        return self.__kodeKiosList
    
    def setKodeKiosList(self, kodeKiosList):
        self.__kodeKiosList = kodeKiosList
        
    def tambah_kode_kios(self, kodeKios):
        self.__kodeKiosList.append(kodeKios)

# ==========================================================


# =============================================================
class Karyawan(Human):
    def __init__(self, NoKTP, nama, alamat, liburShift):
        super().__init__(NoKTP, nama, alamat)
        self.__liburShift = liburShift
    
    def getLiburShift(self):
        return self.__liburShift
    
    def setLiburShift(self, liburShift):
        self.__liburShift = liburShift

class KaryawanPengelola(Karyawan):
    def __init__(self, kodeKaryawanPengelola, NoKTP, nama, alamat, liburShift):
        super().__init__(NoKTP, nama, alamat, liburShift)
        self.__kodeKaryawanPengelola = kodeKaryawanPengelola

    def getKodeKaryawanPengelola(self):
        return self.__kodeKaryawanPengelola
    
    def setKodeKaryawanPengelola(self, kodeKaryawanPengelola):
        self.__kodeKaryawanPengelola = kodeKaryawanPengelola


class KaryawanKios(Karyawan):
    def __init__(self, kodeKaryawanKios, NoKTP, nama, alamat, liburShift):
        super().__init__(NoKTP, nama, alamat, liburShift)
        self.__kodeKaryawanKios = kodeKaryawanKios

    def getKodeKaryawanKios(self):
        return self.__kodeKaryawanKios
    
    def setKodeKaryawanKios(self, kodeKaryawanKios):
        self.__kodeKaryawanKios = kodeKaryawanKios
# ==================================================



# =================================================
class Menu:
    def __init__(self, kodeKios, harga, keterangan):
        self.__kodeKios = kodeKios
        self.__harga = harga
        self.__keterangan = keterangan
    
    def getKodeKios(self):
        return self.__kodeKios

    def setKodeKios(self, kodeKios):
        self.__kodeKios = kodeKios

    def getHarga(self):
        return self.__harga

    def setHarga(self, harga):
        self.__harga = harga

    def getKeterangan(self):
        return self.__keterangan

    def setKeterangan(self, keterangan):
        self.__keterangan = keterangan

class Makanan(Menu):
    def __init__(self, kodeMakanan, kodeKios, namaMakanan, harga, keterangan):
        super().__init__(kodeKios, harga, keterangan)
        self.__kodeMakanan = kodeMakanan
        self.__namaMakanan = namaMakanan
    
    def getKodeMakanan(self):
        return self.__kodeMakanan
    
    def setKodeMakanan(self, kodeMakanan):
        self.__kodeMakanan = kodeMakanan
    
    def getNamaMakanan(self):
        return self.__namaMakanan
    
    def setNamaMakanan(self, namaMakanan):
        self.__namaMakanan = namaMakanan


class Minuman(Menu):
    def __init__(self, kodeMinuman, kodeKios, namaMinuman, harga, keterangan):
        super().__init__(kodeKios, harga, keterangan)
        self.__kodeMinuman = kodeMinuman
        self.__namaMinuman = namaMinuman
    
    def getKodeMinuman(self):
        return self.__kodeMinuman
    
    def setKodeMinuman(self, kodeMinuman):
        self.__kodeMinuman = kodeMinuman
    
    def getNamaMinuman(self):
        return self.__namaMinuman
    
    def setNamaMinuman(self, namaMinuman):
        self.__namaMinuman = namaMinuman
# =================================================================
class Transaksi:
    def __init__(self, kodeKios, tanggal, kodeKaryawanKios, kodeKaryawanPengelola):
        self.kodeKios = kodeKios
        self.tanggal = tanggal
        self.kodeMakanan = []
        self.kodeMinuman = []
        self.kodeKaryawanKios = kodeKaryawanKios
        self.kodeKaryawanPengelola = kodeKaryawanPengelola
        
    def set_kode_kios(self, kodeKios):
        self.kodeKios = kodeKios
        
    def get_kode_kios(self):
        return self.kodeKios
        
    def set_tanggal(self, tanggal):
        self.tanggal = tanggal
        
    def get_tanggal(self):
        return self.tanggal
        
    def tambah_makanan(self, makanan):
        self.kodeMakanan.append(makanan)
        
    def tambah_minuman(self, minuman):
        self.kodeMinuman.append(minuman)
        
    def set_kode_karyawan_kios(self, kodeKaryawanKios):
        self.kodeKaryawanKios = kodeKaryawanKios
        
    def get_kode_karyawan_kios(self):
        return self.kodeKaryawanKios
        
    def set_kode_karyawan_pengelola(self, kodeKaryawanPengelola):
        self.kodeKaryawanPengelola = kodeKaryawanPengelola
        
    def get_kode_karyawan_pengelola(self):
        return self.kodeKaryawanPengelola


class PembagianTransaksiPerHari:
    def init(self, kode_kios, omset_dibagikan, bagian_pengelola, tanggal, pemilik, transaksi):
        self.kode_kios = kode_kios
        self.omset_dibagikan = omset_dibagikan
        self.bagian_pengelola = bagian_pengelola
        self.tanggal = tanggal
        self.pemilik = pemilik
        self.transaksi = transaksi

    def tambah_transaksi(self, transaksi_baru):
        self.transaksi.append(transaksi_baru)

    def hitung_total_transaksi(self):
        return sum(transaksi.harga for transaksi in self.transaksi)

    # setter dan getter untuk atribut kode_kios
    def set_kode_kios(self, kode_kios):
        self.kode_kios = kode_kios

    def get_kode_kios(self):
        return self.kode_kios

    # setter dan getter untuk atribut omset_dibagikan
    def set_omset_dibagikan(self, omset_dibagikan):
        self.omset_dibagikan = omset_dibagikan

    def get_omset_dibagikan(self):
        return self.omset_dibagikan

    # setter dan getter untuk atribut bagian_pengelola
    def set_bagian_pengelola(self, bagian_pengelola):
        self.bagian_pengelola = bagian_pengelola

    def get_bagian_pengelola(self):
        return self.bagian_pengelola

    # setter dan getter untuk atribut tanggal
    def set_tanggal(self, tanggal):
        self.tanggal = tanggal

    def get_tanggal(self):
        return self.tanggal

    # setter dan getter untuk atribut pemilik
    def set_pemilik(self, pemilik):
        self.pemilik = pemilik

    def get_pemilik(self):
        return self.pemilik

    # setter dan getter untuk atribut transaksi
    def set_transaksi(self, transaksi):
        self.transaksi = transaksi

    def get_transaksi(self):
        return self.transaksi

    
