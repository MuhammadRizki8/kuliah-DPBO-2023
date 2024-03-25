class Tabel:
    def __init__(self, baris=0, kolom=0):
        self.baris = baris
        self.kolom = kolom

    def set_baris(self, baris):
        self.baris = baris

    def set_kolom(self, kolom):
        self.kolom = kolom

    def get_baris(self):
        return self.baris

    def get_kolom(self):
        return self.kolom

    def buat_baris(self, isi, max, garis, type):#membuat tampilan baris tabel
        for i in range(garis + 13):#buat garis atas
            print(type, end="")
        print("")
        for i in range(len(isi)):
            print("| ", end="")
            print(isi[i], end=" ")#tampilkan isi data
            for j in range(max[i] - len(isi[i])):
                print(" ", end="")#tampilkan spasi
        print("|")
        for i in range(garis + 13):
            print(type, end="")#tampilkan garis bawah
        print("")

