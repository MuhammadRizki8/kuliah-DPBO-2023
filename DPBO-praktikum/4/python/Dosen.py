from SivitasAkademik import SivitasAkademik

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
