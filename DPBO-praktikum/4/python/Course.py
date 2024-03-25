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