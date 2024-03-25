import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // membuat objek lukisan
        Lukisan lukisan1 = new Lukisan("001", "001", "Menari di atas Trampolin", "Tentang seorang anak kecil yang menari di atas trampolin");

        // membuat objek kolektor, pelukis, dan club lukisan
        List<Lukisan> koleksiLukisan = new ArrayList<>();
        koleksiLukisan.add(lukisan1);
        KolektorLukisan kolektor1 = new KolektorLukisan("842342131", "Fernando Gotarda", "Bandung", 1998, "Painting Collector", koleksiLukisan);
        Pelukis pelukis1 = new Pelukis("123456789", "Gundala Putra Petir", "Bandung", 2000, "Gundala Collection");
        ClubKolektorLukisan club1 = new ClubKolektorLukisan("Painting Collector", 1998, "Painting Collector Club", "Bandung");

        // membuat objek foto
        Foto foto1 = new Foto("002", "002", "Sinar Matahari Menembus Kabut", "Sebuah foto kabut di pagi hari dengan sinar matahari yang menembus");

        // membuat objek kolektor, fotografer, dan klub foto
        List<Foto> koleksiFoto = new ArrayList<>();
        koleksiFoto.add(foto1);
        KolektorFoto kolektor2 = new KolektorFoto("012345678", "Larasati", "Jakarta", 2005, "Photography Enthusiast", koleksiFoto);
        Fotografer fotografer1 = new Fotografer("987654321", "Budi Santoso", "Jakarta", 2010, "Budi Collection");
        ClubKolektorFoto club2 = new ClubKolektorFoto("Photography Enthusiast", 2005, "Photography Enthusiast Club", "Jakarta");

        // menampilkan data anggota dan lukisan
        System.out.println("Data Anggota Lukisan:");
        System.out.println("- Nama: " + kolektor1.getNama());
        System.out.println("- NIK: " + kolektor1.getNIK());
        System.out.println("- Alamat: " + kolektor1.getAlamat());
        System.out.println("- Tahun Aktif: " + kolektor1.getTahunAktif());
        System.out.println("- Nama Club: " + kolektor1.getKodeClub());
        System.out.println("- Tahun Berdiri Club: " + club1.getTahunBerdiri());
        System.out.println("- Alamat Club: " + club1.getAlamat());

        System.out.println("Lukisan:");
        for (Lukisan lukisan : koleksiLukisan) {
            System.out.println("- Kode Pelukis: " + pelukis1.getNIK());
            System.out.println("- Kode Lukisan: " + lukisan.getKodeLukisan());
            System.out.println("- Judul Lukisan: " + lukisan.getJudulLukisan());
            System.out.println("- Deskripsi: " + lukisan.getDeskripsi());
        }

        System.out.println("\nData Anggota Foto:");
        System.out.println("- Nama: " + kolektor2.getNama());
        System.out.println("- NIK: " + kolektor2.getNIK());
        System.out.println("- Alamat: " + kolektor2.getAlamat());
        System.out.println("- Tahun Aktif: " + kolektor2.getTahunAktif());
        System.out.println("- Nama Club: " + kolektor2.getKodeClub());
        System.out.println("- Tahun Berdiri Club: " + club2.getTahunBerdiri());
        System.out.println("- Alamat Club: " + club2.getAlamat());
        System.out.println("Foto:");
        for (Foto foto : koleksiFoto) {
            System.out.println("- Kode Fotografer: " + fotografer1.getNIK());
            System.out.println("- Kode Foto: " + foto.getKodeFoto());
            System.out.println("- Judul Foto: " + foto.getJudulFoto());
            System.out.println("- Deskripsi: " + foto.getDeskripsi());
        }
    }
}    