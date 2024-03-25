template <class T> 
class Aritmatika{
    private:
    T x; // koordinat x
    T y; // koordinat y
    public:
    Aritmatika();
    Aritmatika (T xp, T yp);
    T getX();
    void setX (T xp);
    T getY();
    void setY (T yp);
    T tambah();
    T kurang();
    T kali();
    T bagi();
    ~Aritmatika();
};