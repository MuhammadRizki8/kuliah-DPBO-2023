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
