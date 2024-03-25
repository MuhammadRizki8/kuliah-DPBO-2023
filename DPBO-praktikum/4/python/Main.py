# import class yang dibutuhkan
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from Course import Course
from ProgramStudi import ProgramStudi

# membuat beberapa objek mahasiswa
mhs1 = Mahasiswa('2107922', 'Andi', 'L', 'FPMIPA', 'Universitas Pendidikan Indonesia', 'andi@upi.edu')
mhs2 = Mahasiswa('2107923', 'Budi', 'L', 'FPEB', 'Universitas Pendidikan Indonesia', 'budi@upi.edu')
mhs3 = Mahasiswa('2107924', 'Cici', 'P', 'FIP', 'Universitas Pendidikan Indonesia', 'cici@upi.edu')
mhs4 = Mahasiswa('2107925', 'Dewi', 'P', 'FIP', 'Universitas Pendidikan Indonesia', 'dewi@upi.edu')


# membuat beberapa objek dosen
dsn1 = Dosen('001', '123', 'Dr. Ahmad', 'L', 'FPMIPA', 'S3', 'Artificial Intelligence', 'Universitas Pendidikan Indonesia', 'ahmad@upi.edu')
dsn2 = Dosen('002', '456', 'Dr. Roni', 'L', 'FPEB', 'S2', 'Ekonomi Pembangunan', 'Universitas Pendidikan Indonesia', 'budi@upi.edu')
dsn3 = Dosen('003', '789', 'Prof. Nana', 'P', 'FIP', 'S3', 'Psikologi Klinis', 'Universitas Pendidikan Indonesia', 'cici@upi.edu')


# membuat beberapa objek course
course1 = Course('Pemrograman Berorientasi Objek', dsn1)
course2 = Course('Ekonomi Mikro', dsn2)
course3 = Course('Psikologi Anak', dsn3)

# menambahkan mahasiswa ke dalam course
course1.add_mahasiswa(mhs1)
course1.add_mahasiswa(mhs2)
course2.add_mahasiswa(mhs3)
course3.add_mahasiswa(mhs3)
course3.add_mahasiswa(mhs4)

# membuat beberapa objek program studi
prodi1 = ProgramStudi('Ilmu Komputer', 'ILK')
prodi2 = ProgramStudi('Ekonomi', 'EKO')
prodi3 = ProgramStudi('Psikologi', 'PSI')

# menambahkan course ke dalam program studi
prodi1.add_course(course1)
prodi2.add_course(course2)
prodi3.add_course(course3)

print("=======================================")
# menampilkan data mahasiswa
print('Daftar Mahasiswa:')
for mhs in [mhs1, mhs2, mhs3, mhs4]:
    print("---------------------------------------")
    print("NIM         : "+mhs.get_nim())
    print("Nama        : "+mhs.get_nama())
    print("Fakultas    : "+mhs.get_fakultas())
    print("Universitas : "+mhs.get_asal_universitas())
print("=======================================")

# menampilkan data dosen
print("\n=======================================")
print('Daftar Dosen:')
for dsn in [dsn1, dsn2, dsn3]:
    print("---------------------------------------")
    print("NIP                 : "+dsn.get_nip())
    print("Nama                : "+dsn.get_nama())
    print("Jenis Kelamin       : "+dsn.get_jenis_kelamin())
    print("Fakultas            : "+dsn.get_fakultas())
    print("Pendidikan Terakhir : "+dsn.get_pend_terakhir())
    print("Keahlian            : "+dsn.get_keahlian())

print("=======================================")

# menampilkan data course
print("\n=======================================")
print('Daftar Course:')
for course in [course1, course2, course3]:
    print("---------------------------------------")
    print("Nama              : "+course.get_nama_matakuliah())
    print("Dosen Pengampu    : "+course.get_dosen().get_nama())
    print('Daftar Mahasiswa  :')
    # tampilkan list mahasiswanya
    for mhs in course.get_mahasiswa():
        print(f'                   -> {mhs.get_nama()}')
print("=======================================")

# menampilkan data program studi
print("\n=======================================")
print('Daftar Program Studi:')
for prodi in [prodi1, prodi2, prodi3]:
    print("---------------------------------------")
    print("Nama          : "+prodi.get_nama_prodi())
    print("Kode          : "+prodi.get_kode())
    print("Daftar Course : ")
    # tampilkan list course nya
    for course in prodi.get_courses():
        print(f'               -> {course.get_nama_matakuliah()}')
        print("                  Daftar Mahasiswa : ")
        # tampilkan list mahasiswanya
        for mhs in course.get_mahasiswa():
            print(f'                                    --> {mhs.get_nama()}')
print("=======================================")
