from CivitasAkademik import CivitasAkademik

class Mahasiswa(CivitasAkademik):
    def __init__(self, NIK, nama, gender, universitas, email, NIM, fakultas, studiProgram):
        super().__init__(NIK, nama, gender, universitas, email)
        self.NIM = NIM
        self.fakultas = fakultas
        self.studiProgram = studiProgram
    
    def getNIM(self):
        return self.NIM
    
    def setNIM(self, NIM):
        self.NIM = NIM

    def getFakultas(self):
        return self.fakultas
    
    def setFakultas(self, fakultas):
        self.fakultas = fakultas

    def getStudiProgram(self):
        return self.studiProgram
    
    def setStudiProgram(self, studiProgram):
        self.studiProgram = studiProgram
