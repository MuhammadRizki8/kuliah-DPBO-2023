class Human:
    def __init__(self, nik, nama, jenis_kelamin):
        self._nik = nik
        self._nama = nama
        self._jenis_kelamin = jenis_kelamin

    def get_nik(self):
        return self._nik

    def set_nik(self, nik):
        self._nik = nik

    def get_nama(self):
        return self._nama

    def set_nama(self, nama):
        self._nama = nama

    def get_jenis_kelamin(self):
        return self._jenis_kelamin

    def set_jenis_kelamin(self, jenis_kelamin):
        self._jenis_kelamin = jenis_kelamin


class SivitasAkademik(Human):
    def __init__(self, nik, nama, jenis_kelamin, asal_universitas, email_edu):
        super().__init__(nik, nama, jenis_kelamin)
        self._asal_universitas = asal_universitas
        self._email_edu = email_edu

    def set_asal_universitas(self, asal_universitas):
        self._asal_universitas = asal_universitas

    def get_asal_universitas(self):
        return self._asal_universitas

    def set_email_edu(self, email_edu):
        self._email_edu = email_edu

    def get_email_edu(self):
        return self._email_edu

class Mahasiswa(SivitasAkademik):
    def __init__(self, nim, nama, jenis_kelamin, fakultas, asal_universitas, email_edu):
        super().__init__(None, nama, jenis_kelamin, asal_universitas, email_edu)
        self._nim = nim
        self._fakultas = fakultas
        self._prodi = None

    def get_nim(self):
        return self._nim

    def set_nim(self, nim):
        self._nim = nim

    def get_fakultas(self):
        return self._fakultas

    def set_fakultas(self, fakultas):
        self._fakultas = fakultas

    def get_prodi(self):
        return self._prodi

    def set_prodi(self, prodi):
        self._prodi = prodi


class Dosen(SivitasAkademik):
    def __init__(self, nik, nip, nama, jenis_kelamin, fakultas, pend_terakhir, keahlian, asal_universitas, email_edu):
        super().__init__(nik, nama, jenis_kelamin, asal_universitas, email_edu)
        self._nip = nip
        self._fakultas = fakultas
        self._pend_terakhir = pend_terakhir
        self._keahlian = keahlian

    def get_nip(self):
        return self._nip

    def set_nip(self, nip):
        self._nip = nip

    def get_fakultas(self):
        return self._fakultas

    def set_fakultas(self, fakultas):
        self._fakultas = fakultas

    def get_pend_terakhir(self):
        return self._pend_terakhir

    def set_pend_terakhir(self, pend_terakhir):
        self._pend_terakhir = pend_terakhir

    def get_keahlian(self):
        return self._keahlian

    def set_keahlian(self, keahlian):
        self._keahlian = keahlian


class Course:
    def __init__(self, nama_matakuliah, dosen):
        self._nama_matakuliah = nama_matakuliah
        self._dosen = dosen
        self._mahasiswa = []

    def get_nama_matakuliah(self):
        return self._nama_matakuliah
    
    def set_nama_matakuliah(self, nama_matakuliah):
        self._nama_matakuliah = nama_matakuliah

    def get_dosen(self):
        return self._dosen

    def set_dosen(self, dosen):
        self._dosen = dosen

    def get_mahasiswa(self):
        return self._mahasiswa

    def add_mahasiswa(self, mahasiswa):
        self._mahasiswa.append(mahasiswa)

    def remove_mahasiswa(self, mahasiswa):
        if mahasiswa in self._mahasiswa:
            self._mahasiswa.remove(mahasiswa)

class ProgramStudi:
    def __init__(self, nama_prodi, kode):
        self._nama_prodi = nama_prodi
        self._kode = kode
        self._courses = []

    def get_nama_prodi(self):
        return self._nama_prodi

    def set_nama_prodi(self, nama_prodi):
        self._nama_prodi = nama_prodi

    def get_kode(self):
        return self._kode

    def set_kode(self, kode):
        self._kode = kode

    def get_courses(self):
        return self._courses

    def add_course(self, course):
        self._courses.append(course)

    def remove_course(self, course):
        if course in self._courses:
            self._courses.remove(course)

