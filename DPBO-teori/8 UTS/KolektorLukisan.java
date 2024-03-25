import java.util.*;

public class KolektorLukisan implements Kolektor{
    private String NIK;
    private String nama;
    private String alamat;
    private int tahunAktif;
    private String kodeClub;
    private List<Lukisan> koleksiLukisan;

    public KolektorLukisan(String NIK, String nama, String alamat, int tahunAktif, String kodeClub, List<Lukisan> koleksiLukisan) {
        this.NIK = NIK;
        this.nama = nama;
        this.alamat = alamat;
        this.tahunAktif = tahunAktif;
        this.kodeClub = kodeClub;
        this.koleksiLukisan = koleksiLukisan;
    }

    public String getNIK() {
        return NIK;
    }

    public String getNama() {
        return nama;
    }

    public String getAlamat() {
        return alamat;
    }

    public int getTahunAktif() {
        return tahunAktif;
    }

    public String getKodeClub() {
        return kodeClub;
    }

    public List<Lukisan> getKoleksiLukisan() {
        return koleksiLukisan;
    }
}
