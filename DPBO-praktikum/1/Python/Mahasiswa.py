class Mahasiswa:

    __name=""
    __nim=""
    __prodi=""
    __fakultas=""

    def __init__(self, name="", nim="", prodi="", fakultas=""):
        self.__name=name
        self.__nim=nim
        self.__prodi=prodi
        self.__fakultas=fakultas

    def get_name(self):
        return self.__name
    
    def get_nim(self):
        return self.__nim
    
    def get_prodi(self):
        return self.__prodi
    
    def get_fakultas(self):
        return self.__fakultas

    def set_name(self, name):
        self.__name=name

    def set_nim(self, nim):
        self.__nim=nim

    def set_prodi(self, prodi):
        self.__prodi=prodi

    def set_fakultas(self, fakultas):
        self.__fakultas=fakultas


