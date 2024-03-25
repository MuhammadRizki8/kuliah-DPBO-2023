<?php
class Mahasiswa
{
  private $nama;
  private $nim;
  private $prodi;
  private $fakultas;
  private $foto_profil;

  public function __construct($nama, $nim, $prodi, $fakultas, $foto_profil) {
      $this->nama = $nama;
      $this->nim = $nim;
      $this->prodi = $prodi;
      $this->fakultas = $fakultas;
      $this->foto_profil = $foto_profil;
  }

  public function getName() {
      return $this->nama;
  }

  public function getNim() {
      return $this->nim;
  }

  public function getProdi() {
      return $this->prodi;
  }

  public function getFakultas() {
      return $this->fakultas;
  }

  public function getFotoProfil() {
      return $this->foto_profil;
  }

  public function setName($nama) {
      $this->nama = $nama;
  }

  public function setNim($nim) {
      $this->nim = $nim;
  }

  public function setProdi($prodi) {
      $this->prodi = $prodi;
  }

  public function setFakultas($fakultas) {
      $this->fakultas = $fakultas;
  }

  public function setFotoProfil($foto_profil) {
      $this->foto_profil = $foto_profil;
  }
}
?>