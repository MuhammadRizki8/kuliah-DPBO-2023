public class ClubKolektorFoto implements Club {
    private String kodeClub;
    private int tahunBerdiri;
    private String namaClub;
    private String alamat;

    public ClubKolektorFoto(String kodeClub, int tahunBerdiri, String namaClub, String alamat) {
        this.kodeClub = kodeClub;
        this.tahunBerdiri = tahunBerdiri;
        this.namaClub = namaClub;
        this.alamat = alamat;
    }

    @Override
    public String getKodeClub() {
        return kodeClub;
    }

    @Override
    public int getTahunBerdiri() {
        return tahunBerdiri;
    }

    @Override
    public String getNamaClub() {
        return namaClub;
    }

    @Override
    public String getAlamat() {
        return alamat;
    }
}