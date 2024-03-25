from SivitasAkademik import SivitasAkademik

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