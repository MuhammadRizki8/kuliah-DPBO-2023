from Class import *

resyad = Mahasiswa("123456789", "2107943", "Resyad", "Laki-laki", "Ilmu Komputer", "FPMIPA", "Universitas Pendidikan Indonesia", "resyad@upi.edu", "Lenovo IdeaPad S145")
resyad.tambah_textbook("Algoritma dan Pemrograman Dasar")
resyad.tambah_textbook("Algoritma dan Pemrograman Menengah")

bem =BEM("BEM nya pahri", "2022-2023")
pahri = BEM_member("12345678", "2107942", "Pahri", "Laki-laki", "Ilmu Komputer", "FPMIPA", "Universitas Pendidikan Indonesia", "pahri@upi.edu", "Acer Nitro 5", bem, "Kadiv Bindang X")
bem.tambah_anggota(pahri)
pahri.tambah_textbook("Pengantar Sistem Basis Data")

rose = Dosen("123456789", "12345678", "Mrs. Rose", "Perempuan", "FPMIPA", "S3 Ilmu Komputer", "Jaringan Komputer", "Universitas Pendidikan Indonesia", "rose@upi.edu", "Asus VivoBook S14", "Spidol")
rose.add_matkul_diampu("DPBO")
rose.add_matkul_diampu("Stuktur Data")
rose.add_matkul_diampu("ALPRO 2")
rose.add_matkul_diampu("ALPRO 1")

mila = Assistant("12345677", "20211234", "Mila", "Perempuan", "Ilmu Komputer", "FPMIPA", "Universitas Pendidikan Indonesia", "mila@upi.edu", "Lenovo Thinkpad X1 Carbon", rose)
mila.tambah_textbook("Buku Sistem Operasi")

engclub = EnglishClub("English Club", "Kemakom English Club ini merupakan komunitas baru yang ada di Kemakom dan bergerak di bidang bahasa, khususnya bahasa Inggris.")
gatsby = EnglishClubMembers("123456", "190219", "gatsby", "Laki-laki", "Ilmu Komputer", "FPMIPA", "Universitas Pendidikan Indonesia", "gatsby@upi.edu", "Lenovo IdeaPad 3", engclub)
engclub.tambah_anggota(gatsby)
gatsby.tambah_textbook("Buku Analisis dan Desain Algoritma")

angga = EnglishClubMembers("123457", "190220", "Angga", "Laki-laki", "Ilmu Komputer", "FPMIPA", "Universitas Pendidikan Indonesia", "angga@upi.edu", "Acer Aspire 5", engclub)
engclub.tambah_anggota(angga)
angga.tambah_textbook("Buku Desain Pemrograman Berorientasi Objek dengan Python")

mahasiswa_list = [resyad, pahri, angga, gatsby, mila]