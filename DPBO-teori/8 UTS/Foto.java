public class Foto implements KaryaSeni {
    private String kodeFotografer;
    private String kodeFoto;
    private String judulFoto;
    private String deskripsi;

    public Foto(String kodeFotografer, String kodeFoto, String judulFoto, String deskripsi) {
        this.kodeFotografer = kodeFotografer;
        this.kodeFoto = kodeFoto;
        this.judulFoto = judulFoto;
        this.deskripsi = deskripsi;
    }

    public String getKodeFotografer() {
        return kodeFotografer;
    }

    public String getKodeFoto() {
        return kodeFoto;
    }

    @Override
    public String getKode() {
        return kodeFoto;
    }

    public String getJudulFoto() {
        return judulFoto;
    }

    @Override
    public String getJudul() {
        return judulFoto;
    }

    @Override
    public String getDeskripsi() {
        return deskripsi;
    }
}