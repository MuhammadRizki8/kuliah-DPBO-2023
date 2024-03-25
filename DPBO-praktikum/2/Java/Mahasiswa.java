public class Mahasiswa extends CivitasAkademik {
    protected String NIM;
    protected String fakultas;
    protected String studiProgram;

    // Konstruktor
    public Mahasiswa(String NIK, String nama, String gender, String universitas, String email, String NIM, String fakultas, String studiProgram) {
        super(NIK, nama, gender, universitas, email);
        this.NIM = NIM;
        this.fakultas = fakultas;
        this.studiProgram = studiProgram;
    }

    // Getter untuk NIM
    public String getNIM() {
        return NIM;
    }

    // Getter untuk fakultas
    public String getFakultas() {
        return fakultas;
    }

    // Getter untuk program studi
    public String getStudiProgram() {
        return studiProgram;
    }
}
