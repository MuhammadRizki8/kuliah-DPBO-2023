/**
 * Mahasiswa
 */
public class Mahasiswa {
    private String nama;
    private String nim;
    private String prodi;
    private String fakultas;

    public Mahasiswa(){

    }
    public Mahasiswa(String nama, String nim, String prodi, String fakultas){
        this.nama=nama;
        this.nim=nim;
        this.prodi=prodi;
        this.fakultas=fakultas;
    }
    public void set_nama(String nama){
        this.nama=nama;
    }
    public String get_nama(){
        return this.nama;
    }
    public void set_nim(String nim){
        this.nim=nim;
    }
    public String get_nim(){
        return this.nim;
    }
    public void set_prodi(String prodi){
        this.prodi=prodi;
    }
    public String get_prodi(){
        return this.prodi;
    }
    public void set_fakultas(String fakultas){
        this.fakultas=fakultas;
    }
    public String get_fakultas(){
        return this.fakultas;
    }

}