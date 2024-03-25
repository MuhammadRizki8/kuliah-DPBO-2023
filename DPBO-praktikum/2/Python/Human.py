class Human:
    def __init__(self, NIK, nama, gender):
        self.NIK = NIK
        self.nama = nama
        self.gender = gender

    def getNIK(self):
        return self.NIK
    
    def setNIK(self, NIK):
        self.NIK = NIK
        
    def getNama(self):
        return self.nama

    def setNama(self, nama):
        self.nama = nama
        
    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender
