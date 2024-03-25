public class Human {
    protected String NIK;
    protected String nama;
    protected String gender;

    // Konstruktor
    public Human(String NIK, String nama, String gender) {
        this.NIK = NIK;
        this.nama = nama;
        this.gender = gender;
    }

    // Getter untuk NIK
    public String getNIK() {
        return NIK;
    }
    public String setNIK(String NIK) {
        return this.NIK=NIK;
    }
    
    // Getter untuk nama
    public String getnama() {
        return nama;
    }
    public String setNama(String nama) {
        return this.nama=nama;
    }

    // Getter untuk jenis kelamin
    public String getGender() {
        return gender;
    }
    public String setGender(String gender) {
        return this.gender=gender;
    }
}
