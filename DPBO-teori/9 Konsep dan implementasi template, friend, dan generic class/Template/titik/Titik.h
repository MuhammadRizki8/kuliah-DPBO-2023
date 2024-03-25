template <class T> 
class Titik{
    private:
    T x; // koordinat x
    T y; // koordinat y
    public:
    Titik();
    Titik (T xp, T yp);
    T getX();
    void setX (T xp);
    T getY();
    void setY (T yp);
    ~Titik();
};