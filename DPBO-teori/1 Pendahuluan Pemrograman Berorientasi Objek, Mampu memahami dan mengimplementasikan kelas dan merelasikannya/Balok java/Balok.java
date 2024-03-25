/**
 * Balok
 */
public class Balok {
    private int panjang;
    private int lebar;
    private int tinggi;

    public Balok(){
        
    }
    public Balok(int panjang, int lebar, int tinggi){
        this.panjang=panjang;
        this.lebar=lebar;
        this.tinggi=tinggi;
    }
    public void set_panjang(int panjang){
        this.panjang=panjang;
    }
    public void set_lebar(int lebar){
        this.lebar=lebar;
    }
    public void set_tinggi(int tinggi){
        this.tinggi=tinggi;
    }
    public int get_panjang(){
        return this.panjang;
    }
    public int get_lebar(){
        return this.lebar;
    }
    public int get_tinggi(){
        return this.tinggi;
    }
    public int volume(){
        return this.panjang*this.lebar*this.tinggi;
    }
    public int luas(){
        return ((2*panjang*lebar)+(2*panjang*tinggi)+(2*lebar*tinggi));
    }
}