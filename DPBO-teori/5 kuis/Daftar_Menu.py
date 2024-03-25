from Classes import *

# Loop untuk menampilkan setiap objek

# Membuat objek Makanan
makanan1 = Makanan("MK1", "K01", "Nasi Goreng", 15000, "Nasi goreng dengan bumbu rempah yang khas")
makanan2 = Makanan("MK2", "K01", "Mie Goreng", 12000, "Mie goreng dengan saus yang pedas")
makanan3 = Makanan("MK3", "K02", "Ayam Geprek", 18000, "Ayam goreng tepung dengan sambal geprek")
makanan4 = Makanan("MK4", "K02", "Bakso", 10000, "Bakso dengan kuah kaldu sapi yang gurih")

# Membuat objek Minuman
minuman1 = Minuman("MN1", "K01", "Es Teh Manis", 5000, "Teh manis yang segar")
minuman2 = Minuman("MN2", "K01", "Es Jeruk", 7000, "Jeruk segar dengan es batu")
minuman3 = Minuman("MN3", "K02", "Es Campur", 10000, "Es campur dengan berbagai macam buah")
minuman4 = Minuman("MN4", "K02", "Es Buah", 12000, "Potongan buah dengan es serut")

# Membuat list objek makanan dan minuman
menu_items = [makanan1, makanan2, makanan3, makanan4, minuman1, minuman2, minuman3, minuman4]


for item in menu_items:
    print("Kode Kios:", item.getKodeKios())
    print("Harga:", item.getHarga())
    print("Keterangan:", item.getKeterangan())
    if isinstance(item, Makanan):
        print("Kode Makanan:", item.getKodeMakanan())
        print("Nama Makanan:", item.getNamaMakanan())
    elif isinstance(item, Minuman):
        print("Kode Minuman:", item.getKodeMinuman())
        print("Nama Minuman:", item.getNamaMinuman())
    print("\n")