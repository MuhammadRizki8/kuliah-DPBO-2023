//import class yang dipakai 
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

// Program utama
public class Main {
    public static void main(String[] args) {
        int n=0;//jumlah data
        ArrayList<Mahasiswa> daftarMahasiswa = new ArrayList<>();//list daftar
        Scanner sc= new Scanner(System.in);
        String[] arrisi=new String[8];//array sementara untuk mengisi
        int[] max=new int[]{0,0,0,0,0,0,0,0};//array string terpanjang perkolom

        System.out.println("Masukan banyak Mahasiswa :");
        //input jumlah mahasiswa
        try{
            n=sc.nextInt();
        }
        catch(Exception e){
            System.out.println("Inputan harus berupa angka!");
        }

        sc.nextLine(); // membersihkan buffer input
        for(int i=0; i<n;i++){
            System.out.println("\n-----------------------------");
            System.out.println("Masukan data mahasiswa ke-"+(i+1)+" :");//input data mahasiswa
            for(int j=0; j<8; j++){
                arrisi[j]=sc.nextLine();
                max[j]=max[j]>arrisi[j].length()?max[j]:arrisi[j].length();//cek nilai string terpanjang
            }
            Mahasiswa mahasiswa1=new Mahasiswa(arrisi[0],arrisi[1],arrisi[2],arrisi[3],arrisi[4],arrisi[5],arrisi[6],arrisi[7]);//buat objek
            daftarMahasiswa.add(mahasiswa1);//tambahkan objek ke list daftar
        }
        

        int max_sum=Arrays.stream(max).sum();//jumlahkan isi array max
        System.out.println("\n-----------------------------");
        System.out.println("Daftar Mahasiswa : ");
        String[] arrheader=new String[]{"NIK", "NAMA", "GENDER", "UNIVERSITAS", "EMAIL", "NIM", "FAKULTAS", "PROGRAM STUDI"};//array untuk header tabel
        for(int i=0; i<4; i++){
            max[i]=max[i]>arrheader[i].length()?max[i]:arrheader[i].length();//cek string terpanjang header
        }

        Tabel tab=new Tabel(n, 8);//buat objek tabel
        tab.buat_baris(arrheader, max, max_sum, '=');//tampilkan tabel header
        for (int i = 0; i < daftarMahasiswa.size(); i++) {//loop
            String[] arrstr=new String[8];//array sementara, diisi oleh data per-mahasiswa 
            arrstr[0]=""+daftarMahasiswa.get(i).getNIK();
            arrstr[1]=""+daftarMahasiswa.get(i).getnama();
            arrstr[2]=""+daftarMahasiswa.get(i).getGender();
            arrstr[3]=""+daftarMahasiswa.get(i).getUniversitas();
            arrstr[4]=""+daftarMahasiswa.get(i).getEmail();
            arrstr[5]=""+daftarMahasiswa.get(i).getNIM();
            arrstr[6]=""+daftarMahasiswa.get(i).getFakultas();
            arrstr[7]=""+daftarMahasiswa.get(i).getStudiProgram();
            tab.buat_baris(arrstr, max, max_sum, '-');//buat tabel mahasiswa
        }
        sc.close();
    }
}

/*
1234567890
Budi
Laki-laki
Universitas Indonesia
budi@ui.ac.id
19001
Fakultas Ilmu Komputer
Teknik Informatika

1234567891
Budha
Laki-laki
Universitas Indonesia
budha@ui.ac.id
1893
Fakultas Ilmu Agama
Agama Budha
 */