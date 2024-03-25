public class Tabel {
    private int baris;
    private int kolom;

    Tabel(){

    }
    Tabel(int baris, int kolom){
        this.baris=baris;
        this.kolom=kolom;
    }
    public void set_baris(int baris){
        this.baris=baris;
    }
    public void set_kolom(int kolom){
        this.kolom=kolom;
    }
    public int get_baris(){
        return this.baris;
    }
    public int get_kolom(){
        return this.kolom;
    }
    public void buat_baris(String[] isi, int[] max, int garis, char type_line){
        int i=0,j=0;

        for(i=0; i<garis+13; i++){
            System.out.print(type_line);
        }
        System.out.println((""));
        for(i=0; i<isi.length; i++){
            System.out.print("| ");
            System.out.print(isi[i]+" ");
            for(j=0;j<max[i]-isi[i].length();j++){
                System.out.print(" ");
            }
        }
        System.out.println("|");
        for(i=0; i<garis+13; i++){
            System.out.print(type_line);
        }
        System.out.println((""));
    }
}
