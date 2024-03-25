class ClubKolektorLukisan implements Club{
    String kodeClub;
    int tahunBerdiri;
    String namaClub;
    String alamat;

    public ClubKolektorLukisan(String kodeClub, int tahunBerdiri, String namaClub, String alamat) {
        this.kodeClub = kodeClub;
        this.tahunBerdiri = tahunBerdiri;
        this.namaClub = namaClub;
        this.alamat = alamat;
    }

    public String getKodeClub() {
        return kodeClub;
    }

    public void setKodeClub(String kodeClub) {
        this.kodeClub = kodeClub;
    }

    public int getTahunBerdiri() {
        return tahunBerdiri;
    }

    public void setTahunBerdiri(int tahunBerdiri) {
        this.tahunBerdiri = tahunBerdiri;
    }

    public String getNamaClub() {
        return namaClub;
    }

    public void setNamaClub(String namaClub) {
        this.namaClub = namaClub;
    }

    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }
}