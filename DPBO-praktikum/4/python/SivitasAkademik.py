from Human import Human

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