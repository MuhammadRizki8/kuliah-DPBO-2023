#include "CivitasAkademik.cpp"
using namespace std;

class Mahasiswa : public CivitasAkademik {
protected:
    string NIM;
    string fakultas;
    string studiProgram;

public:
    Mahasiswa(string NIK, string nama, string gender, string universitas, string email, string NIM, string fakultas, string studiProgram)
        : CivitasAkademik(NIK, nama, gender, universitas, email)
    {
        this->NIM = NIM;
        this->fakultas = fakultas;
        this->studiProgram = studiProgram;
    }

    string getNIM() {
        return NIM;
    }

    string getFakultas() {
        return fakultas;
    }

    string getStudiProgram() {
        return studiProgram;
    }
};