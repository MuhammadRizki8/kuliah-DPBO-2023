<?php
//import kelas mahasiswa
require("Mahasiswa.php");

// membuat array untuk daftar mahasiswa dan untuk header
$daftarMahasiswa = array();
$arrheader = array("NIK", "Nama", "Gender", "Universitas", "Email", "NIM", "Fakultas", "Program Studi", "Foto Profil", "Aksi");

// membuat 3 objek mahasiswa, lalu masukan ke daftar mahasiswa
$mahasiswa1 = new Mahasiswa("12345","Joko Woo","Laki-laki","UGM","joko@gmail.com","123","Fakultas Kehutanan","Kehutanan","https://pbs.twimg.com/media/EhK2lh0U4AAfegI.jpg");
$daftarMahasiswa[] = $mahasiswa1;

$mahasiswa2 = new Mahasiswa("21023","Mas Elon","Laki-Laki","UPI","Elonmas@gmail.com","2107923","FPMIPA","Fiskia","https://pbs.twimg.com/profile_images/1437972915769602049/WhSJZGdC_400x400.jpg");
$daftarMahasiswa[] = $mahasiswa2;

$mahasiswa3 = new Mahasiswa("42112","Bald Podcaster","Laki-Laki","UPI","DedyCahyady@gmail.com","2107925","FPOK","Pendidikan Olahraga","https://upload.wikimedia.org/wikipedia/commons/f/f2/Deddy_Corbuzier%2C_Netmediatama%2C_03.38.jpg");
$daftarMahasiswa[] = $mahasiswa3;

// Proses data yang dikirim dari form
if(isset($_POST['submit'])) {
  // Jika tombol "Tambah" ditekan, tambahkan objek baru ke daftarMahasiswa
  if($_POST['submit'] == 'Tambah') {
    $NIK = $_POST['NIK'];
    $nama = $_POST['nama'];
    $gender = $_POST['gender'];
    $universitas = $_POST['universitas'];
    $email = $_POST['email'];
    $NIM = $_POST['NIM'];
    $fakultas = $_POST['fakultas'];
    $studiProgram = $_POST['studiProgram'];
    $foto_profil = $_POST['foto_profil'];

    $mahasiswa = new Mahasiswa($NIK, $nama, $gender, $universitas, $email, $NIM, $fakultas, $studiProgram, $foto_profil);
    $daftarMahasiswa[] = $mahasiswa;
  }
  // Jika tombol "Hapus" ditekan, hapus mahasiswa dari daftarMahasiswa
  elseif($_POST['submit'] == 'Hapus') {
    $index = $_POST['index'];
    array_splice($daftarMahasiswa, $index, 1);
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
          echo "<td>" . $mahasiswa->getNIK() . "</td>";
          echo "<td>" . $mahasiswa->getNama() . "</td>";
          echo "<td>" . $mahasiswa->getGender() . "</td>";
          echo "<td>" . $mahasiswa->getUniversitas() . "</td>";
          echo "<td>" . $mahasiswa->getEmail() . "</td>";
          echo "<td>" . $mahasiswa->getNim() . "</td>";
          echo "<td>" . $mahasiswa->getFakultas() . "</td>";
          echo "<td>" . $mahasiswa->getStudiProgram() . "</td>";
          echo "<td><img src='" . $mahasiswa->getFotoProfil() . "' alt='Foto Profil'></td>";
          echo "<td>
          <form action='index.php' method='post'>
            <input type='hidden' name='index' value='" . array_search($mahasiswa, $daftarMahasiswa) . "'>
            <button type='submit' name='submit' value='Hapus'>Hapus</button>
          </form>
        </td>";
          echo "</tr>";
        }
        ?>
    </table>
    <br>
    <form method="post">
      <h2>Tambah Mahasiswa</h2>
      
    <label for="NIK">NIK:</label>
    <input type="text" id="NIK" name="NIK" required>

    <label for="nama">Nama:</label>
    <input type="text" id="nama" name="nama" required>
        <br><br>
    <label for="gender">Gender:</label>
    <br>
    <input type="radio" id="gender_laki" name="gender" value="laki-laki" required>
    <label for="gender_laki">Laki-laki</label>
    <input type="radio" id="gender_perempuan" name="gender" value="perempuan" required>
    <label for="gender_perempuan">Perempuan</label>
    <br><br>
    <label for="universitas">Universitas:</label>
    <input type="text" id="universitas" name="universitas" required>

    <label for="email">Email:</label>
    <input type="text" id="email" name="email" required>

    <label for="NIM">NIM:</label>
    <input type="text" id="NIM" name="NIM" required>

    <label for="fakultas">Fakultas:</label>
    <input type="text" id="fakultas" name="fakultas" required>

    <label for="studiProgram">Program Studi:</label>
    <input type="text" id="studiProgram" name="studiProgram" required>
    
    <label for="foto_profil">Foto Profil:</label>
    <input type="text" id="foto_profil" name="foto_profil" required>

      <br>
      <br>
      <input type="submit" name="submit" value="Tambah">
    </form>
  </body>
</html>