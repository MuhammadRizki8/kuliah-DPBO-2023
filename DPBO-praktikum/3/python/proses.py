from obj import *

def proses_mahasiswa(mahasiswa):
    while True:
        print("\n+++++++++++++++++++++++++++++++\nApa yang akan dilakukan",mahasiswa.get_nama(),"?")
        print("1. Tampilkan Data")
        print("2. Eat")
        print("3. Drink")
        print("4. Sleep")
        print("5. Tambah TextBook")
        print("6. Exit")
        act = int(input("Pilihanmu(1-5) : "))
        if act ==1:
            print("---------------------------------------")
            mahasiswa.get_all_data()
            print("---------------------------------------")
        elif act==2:
            print("---------------------------------------")
            mahasiswa.eat()
            print("---------------------------------------")
        elif act==3:
            print("---------------------------------------")
            mahasiswa.drink()
            print("---------------------------------------")
        elif act==4:
            print("---------------------------------------")
            mahasiswa.sleep()
            print("---------------------------------------")
        elif act==5:
            print("---------------------------------------")
            judul=input("Masukan Judul Buku : ")
            mahasiswa.tambah_textbook(judul)
            print(f"Textbook {judul} berhasil ditambahkan")
            print("---------------------------------------")
        elif act==6:
            break
        else:
            print("Input tidak valid. Silakan masukkan angka 1 sampai 6.")
    
def proses_BEM_member(BEM_member):
    while True:
        print("\n+++++++++++++++++++++++++++++++\nApa yang akan dilakukan",BEM_member.get_nama(),"?")
        print("1. Tampilkan Data")
        print("2. Eat")
        print("3. Drink")
        print("4. Sleep")
        print("5. Tambah TextBook")
        print("6. Planing BEM Program")
        print("7. Implementing BEM Program")
        print("8. Attending Evaluations BEM Program")
        print("9. Show Activity List")
        print("10. Exit")
        act = int(input("Pilihanmu(1-10) : "))
        if act ==1:
            print("---------------------------------------")
            BEM_member.get_all_data()
            print("Kabinet BEM      :", BEM_member.get_BEM().get_nama_kabinet())
            print("Periode          :", BEM_member.get_BEM().get_periode())
            print("---------------------------------------")
        elif act==2:
            print("---------------------------------------")
            BEM_member.eat()
            print("---------------------------------------")
        elif act==3:
            print("---------------------------------------")
            BEM_member.drink()
            print("---------------------------------------")
        elif act==4:
            print("---------------------------------------")
            BEM_member.sleep()
            print("---------------------------------------")
        elif act==5:
            print("---------------------------------------")
            judul=input("Masukan Judul Buku : ")
            BEM_member.tambah_textbook(judul)
            print(f"Textbook {judul} berhasil ditambahkan")
            print("---------------------------------------")
        elif act==6:
            print("---------------------------------------")
            activity=input("input activity to planning : ")
            BEM_member.planning_programs(activity)
            print("---------------------------------------")
        elif act==7:
            print("---------------------------------------")
            activity=input("input activity to implementing : ")
            BEM_member.implementing_programs(activity)
            print("---------------------------------------")
        elif act==8:
            print("---------------------------------------")
            activity=input("input activity to evaluate : ")
            BEM_member.attending_evaluations(activity)
            print("---------------------------------------")
        elif act==9:
            print("---------------------------------------")
            print(f"Planning: {BEM_member.get_planning()}")
            print(f"Implementing: {BEM_member.get_implementing()}")
            print(f"Evaluations: {BEM_member.get_evaluations()}")
            print("---------------------------------------")
        elif act==10:
            break
        else:
            print("Input tidak valid. Silakan masukkan angka 1 sampai 10.")

def proses_Assistant(Assistant):
    while True:
        print("\n+++++++++++++++++++++++++++++++\nApa yang akan dilakukan",Assistant.get_nama(),"?")
        print("1. Tampilkan Data")
        print("2. Eat")
        print("3. Drink")
        print("4. Sleep")
        print("5. Tambah Textbook")
        print("6. mengajar")
        print("7. memberikan tugas")
        print("8. Exit")
        act = int(input("Pilihanmu(1-8) : "))
        if act ==1:
            print("---------------------------------------")
            Assistant.get_all_data()
            print(Assistant.get_nama(), "is", Assistant.get_dosen().get_nama(), "assistant")
            print("---------------------------------------")
        elif act==2:
            print("---------------------------------------")
            Assistant.eat()
            print("---------------------------------------")
        elif act==3:
            print("---------------------------------------")
            Assistant.drink()
            print("---------------------------------------")
        elif act==4:
            print("---------------------------------------")
            Assistant.sleep()
            print("---------------------------------------")
        elif act==5:
            print("---------------------------------------")
            judul=input("Masukan Judul Buku : ")
            Assistant.tambah_textbook(judul)
            print(f"Textbook {judul} berhasil ditambahkan")
            print("---------------------------------------")
        elif act==6:
            print("---------------------------------------")
            Assistant.mengajar()
            print("---------------------------------------")
        elif act==7:
            print("---------------------------------------")
            Assistant.memberikan_tugas()
            print("---------------------------------------")
        elif act==8:
            break
        else:
            print("Input tidak valid. Silakan masukkan angka 1 sampai 8.")

def proses_EnglishClubMembers(EnglishClubMembers):
    while True:
        print("\n+++++++++++++++++++++++++++++++\nApa yang akan dilakukan",EnglishClubMembers.get_nama(),"?")
        print("1. Tampilkan Data")
        print("2. Eat")
        print("3. Drink")
        print("4. Sleep")
        print("5. Tambah Textbook")
        print("6. advancing language")
        print("7. planning future programs")
        print("8. Exit")
        act = int(input("Pilihanmu(1-8) : "))
        if act ==1:
            print("---------------------------------------")
            EnglishClubMembers.get_all_data()
            print("Club Name        :", EnglishClubMembers.get_EnglishClub().get_nama_club())
            print("Role             :", EnglishClubMembers.get_role())
            print("---------------------------------------")
        elif act==2:
            print("---------------------------------------")
            EnglishClubMembers.eat()
            print("---------------------------------------")
        elif act==3:
            print("---------------------------------------")
            EnglishClubMembers.drink()
            print("---------------------------------------")
        elif act==4:
            print("---------------------------------------")
            EnglishClubMembers.sleep()
            print("---------------------------------------")
        elif act==5:
            print("---------------------------------------")
            judul=input("Masukan Judul Buku : ")
            EnglishClubMembers.tambah_textbook(judul)
            print(f"Textbook {judul} berhasil ditambahkan")
            print("---------------------------------------")
        elif act==6:
            print("---------------------------------------")
            EnglishClubMembers.advance_language()
            print("---------------------------------------")
        elif act==7:
            print("---------------------------------------")
            EnglishClubMembers.plan_program()
            print("---------------------------------------")
        elif act==8:
            break
        else:
            print("Input tidak valid. Silakan masukkan angka 1 sampai 8.")

def proses_Dosen(Dosen):
    while True:
        print("\n+++++++++++++++++++++++++++++++\nApa yang akan dilakukan",Dosen.get_nama(),"?")
        print("1. Tampilkan Data")
        print("2. Eat")
        print("3. Drink")
        print("4. Sleep")
        print("5. Beri Nilai")
        print("6. Tampilkan Nilai Mahasiswa")
        print("7. Tambah Mata Kuliah yang diampu")
        print("8. Exit")
        act = int(input("Pilihanmu(1-8) : "))
        if act ==1:
            print("---------------------------------------")
            Dosen.get_all_data()
            print("---------------------------------------")
        elif act==2:
            print("---------------------------------------")
            Dosen.eat()
            print("---------------------------------------")
        elif act==3:
            print("---------------------------------------")
            Dosen.drink()
            print("---------------------------------------")
        elif act==4:
            print("---------------------------------------")
            Dosen.sleep()
            print("---------------------------------------")
        elif act==5:
            print("---------------------------------------")
            # tampilkan data mahasiswa yang telah diberi nilai
            print("list mahasiswa:")
            for i, mhs in enumerate(mahasiswa_list):
                print(i+1,".", mhs.get_nama())
            # minta user memilih mahasiswa yang akan diberi nilai

            pilih = int(input("\nMasukkan nomor mahasiswa yang ingin diberi nilai: "))
            while pilih < 1 or pilih > len(mahasiswa_list):
                pilih = int(input("Nomor mahasiswa tidak valid. Masukkan nomor mahasiswa yang ingin diberi nilai: "))
                                    
            matkul=  input("Nama Mata Kuliah :")
            nilai = int(input("Masukkan nilai   : "))
            while nilai < 0 or nilai > 100:
                nilai = int(input("Nilai tidak valid. Masukkan nilai: "))
            Dosen.beri_nilai(mahasiswa_list[pilih-1], matkul, nilai)

            print("---------------------------------------")

        elif act==6:
            print("---------------------------------------")
            for mahasiswa in mahasiswa_list:
                print("=======================\nDaftar nilai", mahasiswa.get_nama())
                nilai_matkul = mahasiswa.get_nilai_matkul()
                if not nilai_matkul:
                    print("Belum ada nilai.")
                else:
                    for matkul, nilai in nilai_matkul:
                        print(matkul, ":", nilai)
                print()
            print("---------------------------------------")

        elif act==7:
            print("---------------------------------------")
            nmatkul=input("Masukan Nama Mata Kuliah : ")
            Dosen.add_matkul_diampu(nmatkul)
            print(f"Mata Kuliah {nmatkul} berhasil ditambahkan")
            print("---------------------------------------")

        elif act==8:
            break
        else:
            print("Input tidak valid. Silakan masukkan angka 1 sampai 7.")