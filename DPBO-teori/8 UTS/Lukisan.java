public class Lukisan implements KaryaSeni {
    private String kodePelukis;
    private String kodeLukisan;
    private String judulLukisan;
    private String deskripsi;

    public Lukisan(String kodePelukis, String kodeLukisan, String judulLukisan, String deskripsi) {
        this.kodePelukis = kodePelukis;
        this.kodeLukisan = kodeLukisan;
        this.judulLukisan = judulLukisan;
        this.deskripsi = deskripsi;
    }

    public String getKodePelukis() {
        return kodePelukis;
    }

    public String getKodeLukisan() {
        return kodeLukisan;
    }

    @Override
    public String getKode() {
        return kodeLukisan;
    }

    public String getJudulLukisan() {
        return judulLukisan;
    }

    @Override
    public String getJudul() {
        return judulLukisan;
    }

    @Override
    public String getDeskripsi() {
        return deskripsi;
    }

    public void setKodePelukis(String kodePelukis) {
        this.kodePelukis = kodePelukis;
    }

    public void setKodeLukisan(String kodeLukisan) {
        this.kodeLukisan = kodeLukisan;
    }

    public void setJudulLukisan(String judulLukisan) {
        this.judulLukisan = judulLukisan;
    }

    public void setDeskripsi(String deskripsi) {
        this.deskripsi = deskripsi;
    }
}
