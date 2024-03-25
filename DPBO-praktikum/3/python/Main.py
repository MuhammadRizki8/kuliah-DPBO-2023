# import class yang dibutuhkan
from proses import *
import os


while True:
    os.system('cls') # untuk Windows, untuk MacOS dan Linux gunakan 'clear'
    print("===================================")
    print("        TP 1 Praktikum DPBO        ")
    print("===================================")
    print("1. Person\n2. BEM\n3. English Club\n4. Exit")
    ops=int(input("Masukan Pilihan Anda (1-4) : "))
    if ops==1:
        while True:
            print("========== Daftar Karakter ==========")
            print("1. Resyad")
            print("2. Pahri")
            print("3. Mila")
            print("4. Gatsby")
            print("5. Angga")
            print("6. Mrs. Rose")
            print("7. Exit")
            user_input = int(input("Pilihanmu(1-7) : "))
            if user_input == 1:
                proses_mahasiswa(resyad)
            elif user_input==2:
                proses_BEM_member(pahri)
            elif user_input==3:
                proses_Assistant(mila)
            elif user_input==4:
                proses_EnglishClubMembers(gatsby)
            elif user_input==5:
                proses_EnglishClubMembers(angga)
            elif user_input==6:
                proses_Dosen(rose)
            elif user_input == 7:
                break
            else:
                print("Input tidak valid. Silakan masukkan angka 1 sampai 7.")
    if ops==2:
        while True:
            print("========== BEM ==========")
            print("1. Informasi BEM")
            print("2. Anggota BEM")
            print("3. Exit")
            user_input = int(input("Pilihanmu(1-3) : "))
            if user_input == 1:
                print("+++++++++++++++++++")
                bem.get_all_data()
                print("+++++++++++++++++++")
            elif user_input==2:
                print("+++++++++++++++++++")
                bem.tampilkan_anggota()
                print("+++++++++++++++++++")
            elif user_input == 3:
                break
            else:
                print("+++++++++++++++++++")
                print("Input tidak valid. Silakan masukkan angka 1 sampai 3.")
                print("+++++++++++++++++++")
    if ops==3:
        while True:
            print("========== English Club ==========")
            print("1. Informasi English Club")
            print("2. Anggota English Club")
            print("3. Exit")
            user_input = int(input("Pilihanmu(1-3) : "))
            if user_input == 1:
                print("+++++++++++++++++++")
                engclub.get_all_data()
                print("+++++++++++++++++++")
            elif user_input==2:
                print("+++++++++++++++++++")
                engclub.tampilkan_anggota()
                print("+++++++++++++++++++")
            elif user_input == 3:
                break
            else:
                print("+++++++++++++++++++")
                print("Input tidak valid. Silakan masukkan angka 1 sampai 3.")
                print("+++++++++++++++++++")

    elif ops == 4:
        break
    else:
        print("Input tidak valid. Silakan masukkan angka 1 sampai 4.")

    

