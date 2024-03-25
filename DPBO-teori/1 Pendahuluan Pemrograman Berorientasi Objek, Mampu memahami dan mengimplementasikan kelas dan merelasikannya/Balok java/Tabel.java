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
    public void buat_baris(String[] isi, int add){
        int i=0,j=0;
        for(i=0; i<isi.length; i++){
            for(j=0; j<isi[i].length()+add; j++){
                System.out.print("-");
            }
        }
        System.out.println((""));
        for(i=0; i<isi.length; i++){
            System.out.print("| ");
            System.out.print(isi[i]);
            for(j=0;j<add-3;j++){
                System.out.print(" ");
            }
            System.out.print("|");
        }
        System.out.println("");
        for(i=0; i<isi.length; i++){
            for(j=0; j<isi[i].length()+add; j++){
                System.out.print("-");
            }
        }
        System.out.println((""));
    }
}
