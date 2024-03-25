from Human import Human
class CivitasAkademik(Human):
    def __init__(self, NIK, nama, gender, universitas, email):
        super().__init__(NIK, nama, gender)
        self.universitas = universitas
        self.email = email
    
    def getUniversitas(self):
        return self.universitas

    def setUniversitas(self, universitas):
        self.universitas = universitas

    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
