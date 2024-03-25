#include <iostream>
#include <string>
using namespace std;

class Human {
    protected:
        string NIK;
        string nama;
        string gender;

    public:
        // Konstruktor
        Human(string NIK, string nama, string gender) {
            this->NIK = NIK;
            this->nama = nama;
            this->gender = gender;
        }

        // Getter untuk NIK
        string getNIK() {
            return NIK;
        }
        void setNIK(string NIK) {
            this->NIK = NIK;
        }
        
        // Getter untuk nama
        string getnama() {
            return nama;
        }
        void setNama(string nama) {
            this->nama = nama;
        }

        // Getter untuk jenis kelamin
        string getGender() {
            return gender;
        }
        void setGender(string gender) {
            this->gender = gender;
        }
};
