#include <iostream>
#include <string>

using namespace std;

class Tabel {
private:
    int baris;
    int kolom;

public:
    Tabel() {
        baris = 0;
        kolom = 0;
    }

    Tabel(int baris, int kolom) {
        this->baris = baris;
        this->kolom = kolom;
    }

    void set_baris(int baris) {
        this->baris = baris;
    }

    void set_kolom(int kolom) {
        this->kolom = kolom;
    }

    int get_baris() {
        return baris;
    }

    int get_kolom() {
        return kolom;
    }

    void buat_baris(string isi[], int max[], int garis, char type_line) {
        int i = 0, j = 0;

        for (i = 0; i < garis + 25; i++) {
            cout << type_line;
        }
        cout << "" << endl;

        for (i = 0; i < 8; i++) {
            cout << "| ";
            cout << isi[i] << " ";
            for (j = 0; j < max[i] - isi[i].length(); j++) {
                cout << " ";
            }
        }
        cout << "|" << endl;

        for (i = 0; i < garis + 25; i++) {
            cout << type_line;
        }
        cout << "" << endl;
    }
};
