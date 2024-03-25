public class Pelukis implements Artis {
    private String NIK;
    private String nama;
    private String alamat;
    private int tahunAktif;
    private String kodeClub;

    public Pelukis(String NIK, String nama, String alamat, int tahunAktif, String kodeClub) {
        this.NIK = NIK;
        this.nama = nama;
        this.alamat = alamat;
        this.tahunAktif = tahunAktif;
        this.kodeClub = kodeClub;
    }

    @Override
    public String getNIK() {
        return NIK;
    }

    @Override
    public void setNIK(String NIK) {
        this.NIK = NIK;
    }

    @Override
    public String getNama() {
        return nama;
    }

    @Override
    public void setNama(String nama) {
        this.nama = nama;
    }

    @Override
    public String getAlamat() {
        return alamat;
    }

    @Override
    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }

    @Override
    public int getTahunAktif() {
        return tahunAktif;
    }

    @Override
    public void setTahunAktif(int tahunAktif) {
        this.tahunAktif = tahunAktif;
    }

    @Override
    public String getKodeClub() {
        return kodeClub;
    }

    @Override
    public void setKodeClub(String kodeClub) {
        this.kodeClub = kodeClub;
    }
}
