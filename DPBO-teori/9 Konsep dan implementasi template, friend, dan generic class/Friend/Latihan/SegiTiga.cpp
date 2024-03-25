class BentukCampur;
class SegiTiga{
private:
    /* data */
    int n;
public:
    SegiTiga(/* args */);
    SegiTiga(int n);
    ~SegiTiga();
    friend class BentukCampur;
};

SegiTiga::SegiTiga(/* args */)
{
    this->n=0;
}
SegiTiga::SegiTiga(int n)
{
    this->n=n;
}


SegiTiga::~SegiTiga()
{
}
