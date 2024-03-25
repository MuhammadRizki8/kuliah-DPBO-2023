<?php
class Human {
    protected $NIK;
    protected $nama;
    protected $gender;

    public function __construct($NIK, $nama, $gender) {
        $this->NIK = $NIK;
        $this->nama = $nama;
        $this->gender = $gender;
    }

    public function getNIK() {
        return $this->NIK;
    }

    public function setNIK($NIK) {
        $this->NIK = $NIK;
    }

    public function getNama() {
        return $this->nama;
    }

    public function setNama($nama) {
        $this->nama = $nama;
    }

    public function getGender() {
        return $this->gender;
    }

    public function setGender($gender) {
        $this->gender = $gender;
    }
}

class CivitasAkademik extends Human {
    protected $universitas;
    protected $email;

    public function __construct($NIK, $nama, $gender, $universitas, $email) {
        parent::__construct($NIK, $nama, $gender);
        $this->universitas = $universitas;
        $this->email = $email;
    }

    public function getUniversitas() {
        return $this->universitas;
    }

    public function setUniversitas($universitas) {
        $this->universitas = $universitas;
    }

    public function getEmail() {
        return $this->email;
    }

    public function setEmail($email) {
        $this->email = $email;
    }
}

class Mahasiswa extends CivitasAkademik {
    protected $NIM;
    protected $fakultas;
    protected $studiProgram;
    protected $fotoProfil;

    public function __construct($NIK, $nama, $gender, $universitas, $email, $NIM, $fakultas, $studiProgram, $fotoProfil) {
        parent::__construct($NIK, $nama, $gender, $universitas, $email);
        $this->NIM = $NIM;
        $this->fakultas = $fakultas;
        $this->studiProgram = $studiProgram;
        $this->fotoProfil=$fotoProfil;
    }

    public function getNIM() {
        return $this->NIM;
    }

    public function setNIM($NIM) {
        $this->NIM = $NIM;
    }

    public function getFakultas() {
        return $this->fakultas;
    }

    public function setFakultas($fakultas) {
        $this->fakultas = $fakultas;
    }

    public function getStudiProgram() {
        return $this->studiProgram;
    }

    public function setStudiProgram($studiProgram) {
        $this->studiProgram = $studiProgram;
    }
    public function getFotoProfil() {
        return $this->fotoProfil;
    }

    public function setFotoProfil($fotoProfil) {
        $this->fotoProfil = $fotoProfil;
    }
}

?>