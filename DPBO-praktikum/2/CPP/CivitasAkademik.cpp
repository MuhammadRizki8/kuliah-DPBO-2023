#include "Human.cpp"
using namespace std;

class CivitasAkademik : public Human {
protected:
    string universitas;
    string email;

public:
    // Konstruktor
    CivitasAkademik(string NIK, string nama, string gender, string universitas, string email)
        : Human(NIK, nama, gender) {
        this->universitas = universitas;
        this->email = email;
    }

    // Getter untuk universitas
    string getUniversitas() {
        return universitas;
    }

    // Getter untuk email
    string getEmail() {
        return email;
    }
};