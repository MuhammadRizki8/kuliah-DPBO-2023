class BentukCampur{
public:
    BentukCampur(){
    }
    ~BentukCampur(){

    }
    void aksesSahabat(SegiTiga s3, SegiEmpat s4){
        for(int i=1; i<=s3.n; i++){
            for(int j=0; j<s3.n-i; j++){
                cout<<"-";
            }
            for(int j=0; j<2*i-1; j++){
                cout<<"*";
            }
            cout<<endl;
        }
        for(int i=0; i<s4.p; i++){
            for(int j=0; j<s4.l; j++){
                cout<<"*";
            }
            cout<<endl;
        }
    }
};
