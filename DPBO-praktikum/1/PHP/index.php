<?php
//import kelas mahasiswa
require("Mahasiswa.php");

// membuat array untuk daftar mahasiswa dan untuk header
$daftarMahasiswa = array();
$arrheader = array("Nama", "NIM", "Prodi", "Fakultas", "Foto Profil");

// membuat 3 objek mahasiswa, lalu masukan ke daftar mahasiswa
$mahasiswa1 = new Mahasiswa("Joko Woo","2107924","Ilmu Politik","FPIPS", "https://pbs.twimg.com/media/EhK2lh0U4AAfegI.jpg");
$daftarMahasiswa[] = $mahasiswa1;

$mahasiswa2 = new Mahasiswa("Mas Elon","2107923","Fiskia","FPMIPA","https://pbs.twimg.com/profile_images/1437972915769602049/WhSJZGdC_400x400.jpg");
$daftarMahasiswa[] = $mahasiswa2;

$mahasiswa3 = new Mahasiswa("Bald Podcaster","2107925","Pendidikan Olahraga","FPOK","https://upload.wikimedia.org/wikipedia/commons/f/f2/Deddy_Corbuzier%2C_Netmediatama%2C_03.38.jpg");
$daftarMahasiswa[] = $mahasiswa3;

// Proses data yang dikirim dari form
if(isset($_POST['submit'])) {
  // Jika tombol "Tambah" ditekan, tambahkan objek baru ke daftarMahasiswa
  if($_POST['submit'] == 'Tambah') {
    $nama = $_POST['nama'];
    $nim = $_POST['nim'];
    $prodi = $_POST['prodi'];
    $fakultas = $_POST['fakultas'];
    $foto_profil = $_POST['foto_profil'];

    $mahasiswa = new Mahasiswa($nama, $nim, $prodi, $fakultas, $foto_profil);
    $daftarMahasiswa[] = $mahasiswa;
  }

}
?>

<html>
  <head>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Daftar Mahasiswa</h1>
    <table>
        <tr>
          <?php
          // menampilkan header dari tabel
          foreach ($arrheader as $header) {
            echo "<th>$header</th>";
          }
          ?>
        </tr>
        <?php
        // menampilkan isi dari tabel, yaitu daftar mahasiswa
        foreach ($daftarMahasiswa as $index => $mahasiswa) {
          echo "<tr>";
          echo "<td>" . $mahasiswa->getName() . "</td>";
          echo "<td>" . $mahasiswa->getNim() . "</td>";
          echo "<td>" . $mahasiswa->getProdi() . "</td>";
          echo "<td>" . $mahasiswa->getFakultas() . "</td>";
          echo "<td><img src='" . $mahasiswa->getFotoProfil() . "' alt='Foto Profil'></td>";
          echo "</tr>";
        }
        ?>
    </table>
    <br>
    <form method="post">
      <h2>Tambah Mahasiswa</h2>
      <label for="nama">Nama:</label>
      <input type="text" id="nama" name="nama" required>
    <label for="nim">NIM:</label>
    <input type="text" id="nim" name="nim" required>

    <label for="prodi">Program Studi:</label>
    <input type="text" id="prodi" name="prodi" required>

    <label for="fakultas">Fakultas:</label>
    <input type="text" id="fakultas" name="fakultas" required>

    <label for="foto_profil">Foto Profil:</label>
    <input type="text" id="foto_profil" name="foto_profil" required>

      <br>
      <br>
      <input type="submit" name="submit" value="Tambah">
    </form>
  </body>
</html>