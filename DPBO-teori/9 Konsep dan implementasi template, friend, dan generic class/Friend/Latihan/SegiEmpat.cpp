class BentukCampur;
class SegiEmpat
{
private:
    /* data */
    int p;
    int l;
public:
    SegiEmpat(/* args */);
    SegiEmpat(int p, int l);
    ~SegiEmpat();
    friend class BentukCampur;
};

SegiEmpat::SegiEmpat(/* args */)
{
    this->p=0;
    this->l=0;
}
SegiEmpat::SegiEmpat(int p, int l)
{
    this->p=p;
    this->l=l;
}


SegiEmpat::~SegiEmpat()
{
}
