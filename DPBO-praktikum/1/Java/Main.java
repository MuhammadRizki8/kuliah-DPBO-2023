//import class yang dipakai
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
public class Main {

    private static void ubahMahasiswa(ArrayList<Mahasiswa> daftarMahasiswa, int[] max) {//update data
        System.out.print("Masukkan NIM mahasiswa yang ingin diubah : ");//input nim data yang akan diupdate
        Scanner sc= new Scanner(System.in);
        String nim = sc.next();
        int index = -1;
        for (int i = 0; i < daftarMahasiswa.size(); i++) {//loop sebanyak isi daftar
            if (daftarMahasiswa.get(i).get_nim().equals(nim)) {//jika ketemu
                index = i;
                break;
            }
        }
        if (index == -1) {//jika tidak ketemu
            System.out.println("Mahasiswa dengan NIM " + nim + " tidak ditemukan\n");
        } 
        else {//jika ketemu
            sc.nextLine(); // membersihkan buffer input
            System.out.print("Masukkan nama baru : ");//isi data baru
            String namaBaru = sc.nextLine();
            System.out.print("Masukkan prodi baru : ");
            String prodiBaru = sc.nextLine();
            System.out.print("Masukkan fakultas baru : ");
            String fakultasBaru = sc.nextLine();
            max[0]=namaBaru.length()>max[0]?namaBaru.length():max[0];//cek string terpanjangnya
            max[2]=prodiBaru.length()>max[2]?prodiBaru.length():max[2];
            max[3]=fakultasBaru.length()>max[3]?fakultasBaru.length():max[3];
            daftarMahasiswa.get(index).set_nama(namaBaru);//set attribut objeknya
            daftarMahasiswa.get(index).set_prodi(prodiBaru);
            daftarMahasiswa.get(index).set_fakultas(fakultasBaru);
            System.out.println("Data mahasiswa berhasil diubah\n");
        }
        // sc.close();
    }
    private static void hapusMahasiswa(ArrayList<Mahasiswa> daftarMahasiswa){//delete data
        System.out.print("Masukkan NIM mahasiswa yang ingin dihapus : ");//minta innputan nim data yang akan dihapus
        Scanner sc= new Scanner(System.in);
        String nim = sc.next();
        int index = -1;
        for (int i = 0; i < daftarMahasiswa.size(); i++) {//cari nim dalam daftar
            if (daftarMahasiswa.get(i).get_nim().equals(nim)) {//berhenti jika ketemu
                index = i;
                break;
            }
        }
        if (index == -1) {//jika tidak ketemu
            System.out.println("Mahasiswa dengan NIM " + nim + " tidak ditemukan\n");
        } 
        else {//jika ketemu
            daftarMahasiswa.remove(index);//hapus data dari daftar
            System.out.println("Data mahasiswa berhasil dihapus\n");
        }  
        // sc.close();      
    }
    public static void main(String[] args) {
        int pil=0, n=0;//pilihan dan banyak data
        ArrayList<Mahasiswa> daftarMahasiswa = new ArrayList<>();//list daftar mahasiswa
        int[] max=new int[]{0,0,0,0};//array strinf terpanjang
        String[] arrisi=new String[]{"", "", "", ""};//array isi
        String[] arrinput=new String[]{"Nama          : ","NIM           : ","Program Studi : ","Fakultas      : "};//array input
        String[] arrheader=new String[]{"NAMA", "NIM", "Prodi", "Fakultas"};//array header
        for(int i=0; i<4; i++){//cari string terpanjang
            max[i]=arrheader[i].length()>max[i]?arrheader[i].length():max[i];
        }
        Scanner sc= new Scanner(System.in);
        do{
            System.out.println("1. Tambah Data");
            System.out.println("2. Tampilkan Daftar Mahasiswa");
            System.out.println("3. Update Data");
            System.out.println("4. Hapus Data");
            System.out.println("5. Keluar");
            System.out.println("-----------------------------");
            System.out.println("Masukan Pilihan(1-5) : ");//meminta input pilihan
            try{
                pil=sc.nextInt();
            }
            catch(Exception e){
                System.out.println("Inputan harus berupa angka!");
            } 
            switch (pil) {//tambah data
                case 1:
                    System.out.println("Masukan banyak Mahasiswa : ");//input jumlah data
                    try{
                        n=sc.nextInt();
                    }
                    catch(Exception e){
                        System.out.println("Inputan harus berupa angka!");
                    }
                    sc.nextLine(); // membersihkan buffer input
                    for(int i=0; i<n;i++){
                        System.out.println("Masukan data mahasiswa ke-"+(i+1)+" :");
                        for(int j=0; j<4; j++){
                            System.out.print(arrinput[j]);
                            arrisi[j]=sc.nextLine();//inputkan data mahasiswa
                            max[j]=max[j]>arrisi[j].length()?max[j]:arrisi[j].length();//cek string terpanjangnya
                        }
                        Mahasiswa temp=new Mahasiswa(arrisi[0], arrisi[1], arrisi[2], arrisi[3]);//buat objek mahasiswanya
                        daftarMahasiswa.add(temp);//tambahkan ke list
                        System.out.println("-----------------------------");
                    }
                    System.out.println("Data berhasil ditambahkan\n");
                    break;
                case 2://tampilkan tabel
                    if(!daftarMahasiswa.isEmpty()){//jika list tidak kosong
                        System.out.println("-----------------------------");
                        int max_sum=Arrays.stream(max).sum();      //jumlah total isi array max       
                        System.out.println("Daftar Mahasiswa : ");
                        Tabel tab=new Tabel(n, 4);//buat objek tabel
                        tab.buat_baris(arrheader, max, max_sum, '=');//tampilkan header
                        for (int i = 0; i < daftarMahasiswa.size(); i++) {
                            String[] arrstr=new String[4];
                            arrstr[0]=""+daftarMahasiswa.get(i).get_nama();//salin attribut ke array
                            arrstr[1]=""+daftarMahasiswa.get(i).get_nim();
                            arrstr[2]=""+daftarMahasiswa.get(i).get_prodi();
                            arrstr[3]=""+daftarMahasiswa.get(i).get_fakultas();
                            tab.buat_baris(arrstr, max, max_sum,'-');//buat isi data
                            }
                    }
                    else{
                        System.out.println("\n=== Daftar masih kosong ===\n");
                    }
                    break;
                case 3://update
                    ubahMahasiswa(daftarMahasiswa, max);
                    break;
                case 4://delete
                    hapusMahasiswa(daftarMahasiswa);
                    break;
                case 5:
                    break;
                default:
                    System.out.println("Masukan inputan dengan benar");
                    break;
            }
            System.out.println("-----------------------------");
        }while(pil!=5);
        System.out.println("=== Terima Kasih ===");
        sc.close();
    }
}
