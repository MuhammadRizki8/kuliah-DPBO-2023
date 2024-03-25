public class CivitasAkademik extends Human {
    protected String universitas;
    protected String email;

    // Konstruktor
    public CivitasAkademik(String NIK, String nama, String gender, String universitas, String email) {
        super(NIK, nama, gender);
        this.universitas = universitas;
        this.email = email;
    }

    // Getter untuk universitas
    public String getUniversitas() {
        return universitas;
    }

    // Getter untuk email
    public String getEmail() {
        return email;
    }
}
