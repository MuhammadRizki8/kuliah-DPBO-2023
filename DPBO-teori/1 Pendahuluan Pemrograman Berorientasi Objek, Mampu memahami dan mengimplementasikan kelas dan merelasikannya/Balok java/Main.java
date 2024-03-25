import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int n=0;
        System.out.println("Masukan banyak balok :");
        Scanner sc= new Scanner(System.in);
        try{
            n=sc.nextInt();
        }
        catch(Exception e){
            System.out.println("Inputan harus berupa angka!");
        }
        Balok[] arrbalok=new Balok[n];
        int p=0,l=0,t=0;
        for(int i=0; i<n;i++){
            System.out.println("Masukan Panjang, Lebar dan Tinggi  balok ke-"+(i+1)+" :");
            try{
                p=sc.nextInt();
            }
            catch(Exception e){
                System.out.println("Inputan harus berupa angka!");
            }
            try{
                l=sc.nextInt();
            }
            catch(Exception e){
                System.out.println("Inputan harus berupa angka!");
            }
            try{
                t=sc.nextInt();
            }
            catch(Exception e){
                System.out.println("Inputan harus berupa angka!");
            }
            arrbalok[i]=new Balok(p, l, t);
        }
        Tabel tab=new Tabel(n, 5);
        for(int i=0;i<n;i++){
            String[] arrstr=new String[5];
            arrstr[0]=""+arrbalok[i].get_panjang();
            arrstr[1]=""+arrbalok[i].get_lebar();
            arrstr[2]=""+arrbalok[i].get_tinggi();
            arrstr[3]=""+arrbalok[i].volume();
            arrstr[4]=""+arrbalok[i].luas();
            tab.buat_baris(arrstr, 5);
        }
    }
}
