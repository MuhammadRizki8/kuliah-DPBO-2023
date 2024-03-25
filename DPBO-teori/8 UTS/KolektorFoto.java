import java.util.*;

public class KolektorFoto implements Kolektor{
    private String NIK;
    private String nama;
    private String alamat;
    private int tahunAktif;
    private String kodeClub;
    private List<Foto> koleksiFoto;

    public KolektorFoto(String NIK, String nama, String alamat, int tahunAktif, String kodeClub, List<Foto> koleksiFoto) {
        this.NIK = NIK;
        this.nama = nama;
        this.alamat = alamat;
        this.tahunAktif = tahunAktif;
        this.kodeClub = kodeClub;
        this.koleksiFoto = koleksiFoto;
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

    public List<Foto> getKoleksiFoto() {
        return koleksiFoto;
    }

    public void setNIK(String nIK) {
        NIK = nIK;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }

    public void setTahunAktif(int tahunAktif) {
        this.tahunAktif = tahunAktif;
    }

    public void setKodeClub(String kodeClub) {
        this.kodeClub = kodeClub;
    }

    public void setKoleksiFoto(List<Foto> koleksiFoto) {
        this.koleksiFoto = koleksiFoto;
    }
}
