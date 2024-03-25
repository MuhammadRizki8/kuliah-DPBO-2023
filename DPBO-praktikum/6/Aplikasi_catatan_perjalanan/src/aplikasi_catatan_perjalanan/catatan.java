/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aplikasi_catatan_perjalanan;
import java.io.Serializable;
/**
 *
 * @author LENOVO
 */
public class catatan extends menu_utama {
    private int id_catatan;
    private String tanggal, lokasi, deskripsi, foto_lokasi, nik, nama;

    public catatan() {
        this.id_catatan = id_catatan;
        this.tanggal = tanggal;
        this.lokasi = lokasi;
        this.deskripsi = deskripsi;
        this.foto_lokasi = foto_lokasi;
        this.nik = nik;
        this.nama = nama;
    }

    public int getId_catatan() {
        return id_catatan;
    }

    public void setId_catatan(int id_catatan) {
        this.id_catatan = id_catatan;
    }

    public String getTanggal() {
        return tanggal;
    }

    public void setTanggal(String tanggal) {
        this.tanggal = tanggal;
    }

    public String getLokasi() {
        return lokasi;
    }

    public void setLokasi(String lokasi) {
        this.lokasi = lokasi;
    }

    public String getDeskripsi() {
        return deskripsi;
    }

    public void setDeskripsi(String deskripsi) {
        this.deskripsi = deskripsi;
    }

    public String getFoto_lokasi() {
        return foto_lokasi;
    }

    public void setFoto_lokasi(String foto_lokasi) {
        this.foto_lokasi = foto_lokasi;
    }

    public String getNik() {
        return nik;
    }

    public void setNik(String nik) {
        this.nik = nik;
    }

    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }
}
