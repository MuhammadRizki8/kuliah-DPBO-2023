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

    def eat(self):
        print(f"{self._nama} is eating")

    def drink(self):
        print(f"{self._nama} is drinking")

    def sleep(self):
        print(f"{self._nama} is sleeping")

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
    def __init__(self, nik ,nim, nama, jenis_kelamin, prodi, fakultas, asal_universitas, email_edu, laptop):
        super().__init__(nik, nama, jenis_kelamin, asal_universitas, email_edu)
        self._nim = nim
        self._fakultas = fakultas
        self._prodi = prodi
        self._laptop = laptop
        self._textbook = []
        self._nilai_matkul = {}

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

    def get_laptop(self):
        return self._laptop

    def set_laptop(self, laptop):
        self._laptop = laptop

    def get_textbook(self):
        return self._textbook

    def set_textbook(self, textbook):
        self._textbook = textbook

    def tambah_textbook(self, textbook):
        self._textbook.append(textbook)

    def set_nilai_matkul(self, matkul, nilai):
        self._nilai_matkul[matkul] = nilai

    def get_nilai_matkul(self):
        return tuple(self._nilai_matkul.items())
    
    def get_all_data(self):
        print("Nama             :", self.get_nama())
        print("NIK              :", self.get_nik())
        print("NIM              :", self.get_nim())
        print("Jenis Kelamin    :", self.get_jenis_kelamin())
        print("Fakultas         :", self.get_fakultas())
        print("Program Studi    :", self.get_prodi())
        print("Asal Universitas :", self.get_asal_universitas())
        print("Email Edu        :", self.get_email_edu())
        print("Laptop           :", self.get_laptop())
        print("Textbook         :", ", ".join(self.get_textbook()))
        print("Nilai Matkul     :", self.get_nilai_matkul())

class BEM:
    def __init__(self, nama_kabinet, periode):
        self.__nama_kabinet = nama_kabinet
        self.__periode = periode
        self.__anggota = []

    def get_nama_kabinet(self):
        return self.__nama_kabinet

    def set_nama_kabinet(self, nama_kabinet):
        self.__nama_kabinet = nama_kabinet

    def get_periode(self):
        return self.__periode

    def set_periode(self, periode):
        self.__periode = periode

    def get_anggota(self):
        return self.__anggota

    def set_anggota(self, anggota):
        self.__anggota = anggota

    def tambah_anggota(self, orang):
        self.__anggota.append(orang)

    def get_all_data(self):
        print(f"Nama Kabinet : {self.__nama_kabinet}")
        print(f"Periode      : {self.__periode}")

    def tampilkan_anggota(self):
        print("List Anggota:")
        for anggota in self.__anggota:
            print(f"- {anggota.get_nama()} sebagai {anggota.get_role()} ")

class BEM_member(Mahasiswa):
    def __init__(self, nik, nim, nama, jenis_kelamin, prodi, fakultas, asal_universitas, email_edu, laptop, BEM, role):
        super().__init__(nik, nim, nama, jenis_kelamin, prodi, fakultas, asal_universitas, email_edu, laptop)
        self._planning = []
        self._implementing = []
        self._evaluations = []
        self._BEM=BEM
        self._role=role

    def set_BEM(self, BEM):
        self._BEM = BEM

    def get_BEM(self):
        return self._BEM
    
    def set_role(self, role):
        self._role = role

    def get_role(self):
        return self._role
    # --------------------------------------------------------------------------------------
    def get_planning(self):
        return self._planning

    def set_planning(self, planning):
        self._planning = planning

    def tambah_planning(self, planning):
        self._planning.append(planning)

    def planning_programs(self, activity):
        self.tambah_planning(activity)
        print(f"{self.get_nama()} is planning {activity}.")
    # -------------------------------------------------------------------------------------
    def get_implementing(self):
        return self._implementing

    def set_implementing(self, implementing):
        self._implementing = implementing

    def tambah_implementing(self, implementing):
        if len(self._planning) == 0:
            print(f"Cannot implement without planning.")
            return
        if implementing not in self._planning:
            print(f"Cannot implement {implementing} because it is not in the planning list.")
            return
        self._implementing.append(implementing)
        print(f"{implementing} has been implemented.")

    def implementing_programs(self, activity):
        if len(self._planning) == 0:
            print(f"No planning found.")
            return
        self.tambah_implementing(activity)
        
    # -------------------------------------------------------------------------------------
    def get_evaluations(self):
        return self._evaluations

    def set_evaluations(self, evaluations):
        self._evaluations = evaluations

    def tambah_evaluations(self, evaluations):
        if len(self._implementing) == 0:
            print(f"Cannot evaluate without implementing.")
            return
        if evaluations not in self._implementing:
            print(f"Cannot implement {evaluations} because it is not in the implementing list.")
            return
        self._evaluations.append(evaluations)
        print(f"{evaluations} has been evaluated.")

    def attending_evaluations(self, activity):
        if len(self._implementing) == 0:
            print(f"No implementing found.")
            return
        self.tambah_evaluations(activity)

class Assistant(Mahasiswa):
    def __init__(self, nik ,nim, nama, jenis_kelamin, prodi, fakultas, asal_universitas, email_edu, laptop, dosen):
        super().__init__(nik, nim, nama, jenis_kelamin, prodi, fakultas, asal_universitas, email_edu, laptop)
        self._dosen = dosen

    def get_dosen(self):
        return self._dosen

    def set_dosen(self, dosen):
        self._dosen = dosen

    def mengajar(self):
        print(f"{self.get_nama()} sedang mengajar sebagai asisten dari {self._dosen.get_nama()}.")

    def memberikan_tugas(self):
        print(f"{self.get_nama()} memberikan tugas sebagai asisten dari {self._dosen.get_nama()}.")

class EnglishClub:
    def __init__(self, nama_club, deskripsi):
        self.__nama_club = nama_club
        self._deskripsi=deskripsi
        self.__anggota = []

    def get_nama_club(self):
        return self.__nama_club

    def set_nama_club(self, nama_club):
        self.__nama_club = nama_club

    def get_deskripsi(self):
        return self.__deskripsi

    def set_deskripsi(self, deskripsi):
        self.__deskripsi = deskripsi

    def get_anggota(self):
        return self.__anggota

    def set_anggota(self, anggota):
        self.__anggota = anggota

    def tambah_anggota(self, anggota_baru):
        self.__anggota.append(anggota_baru)

    def get_all_data(self):
        print(f"Nama Club    : {self.__nama_club}")
        print(f"Deskripsi    : {self._deskripsi}")

    def tampilkan_anggota(self):
        print("List Anggota:")
        for anggota in self.__anggota:
            print(f"- {anggota.get_nama()} sebagai {anggota.get_role()} ")

class EnglishClubMembers(Mahasiswa):
    def __init__(self, nik, nim, nama, jenis_kelamin, prodi, fakultas, asal_universitas, email_edu, laptop, EnglishClub):
        super().__init__(nik, nim, nama, jenis_kelamin, prodi, fakultas, asal_universitas, email_edu, laptop)
        self._role = "member"
        self._EnglishClub=EnglishClub

    def set_role(self, role):
        self._role = role
        
    def get_role(self):
        return self._role
    
    def set_EnglishClub(self, EnglishClub):
        self._EnglishClub = EnglishClub
        
    def get_EnglishClub(self):
        return self._EnglishClub
    
    def advance_language(self):
        print(f"{self.get_nama()} is advancing their language proficiency.")
        
    def plan_program(self):
        print(f"{self.get_nama()} is planning a program for {self.get_EnglishClub().get_nama_club()}.")

class Dosen(SivitasAkademik):
    def __init__(self, nik, nip, nama, jenis_kelamin, fakultas, pend_terakhir, keahlian, asal_universitas, email_edu, laptop, whiteBoardMarker):
        super().__init__(nik, nama, jenis_kelamin, asal_universitas, email_edu)
        self._nip = nip
        self._fakultas = fakultas
        self._pend_terakhir = pend_terakhir
        self._keahlian = keahlian
        self._laptop=laptop
        self._whiteBoardMarker=whiteBoardMarker
        self._matkul_diampu =[]

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

    def get_laptop(self):
        return self._laptop

    def set_laptop(self, laptop):
        self._laptop = laptop

    def get_whiteBoardMarker(self):
        return self._whiteBoardMarker

    def set_whiteBoardMarker(self, whiteBoardMarker):
        self._whiteBoardMarker = whiteBoardMarker
        
    def beri_nilai(self, mhs, matkul, nilai):
        if matkul not in self._matkul_diampu:
            print(f"Dosen {self.get_nama()} tidak mengajar mata kuliah {matkul}. Nilai tidak dapat diberikan.")
            return
        mhs.set_nilai_matkul(matkul, nilai)
        print(f"Nilai pada mata kuliah {matkul} untuk {mhs.get_nama()} telah diberikan.")


    def get_matkul_diampu(self):
        return self._matkul_diampu

    def set_matkul_diampu(self, matkul_diampu):
        self._matkul_diampu = matkul_diampu

    def add_matkul_diampu(self, matkul):
        self._matkul_diampu.append(matkul)

    def get_all_data(self):
        print("Nama                :", self.get_nama())
        print("NIK                 :", self.get_nik())
        print("NIP                 :", self.get_nip())
        print("Jenis Kelamin       :", self.get_jenis_kelamin())
        print("Fakultas            :", self.get_fakultas())
        print("Pendidikan Terakhir :", self.get_pend_terakhir())
        print("Keahlian            :", self.get_keahlian())
        print("Asal Universitas    :", self.get_asal_universitas())
        print("Email Edu           :", self.get_email_edu())
        print("Laptop              :", self.get_laptop())
        print("Whiteboard Marker   :", self.get_whiteBoardMarker())
        print("Mata Kuliah         :", self.get_matkul_diampu())