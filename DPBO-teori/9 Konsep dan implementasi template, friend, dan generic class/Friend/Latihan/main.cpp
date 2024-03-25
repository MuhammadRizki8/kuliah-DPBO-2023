#include <iostream>
using namespace std;
#include "SegiTiga.cpp"
#include "SegiEmpat.cpp"
#include "BentukCampur.cpp"

int main(){
	SegiEmpat s4(3,5);
    SegiTiga s3(3);
	BentukCampur campur;
	
	campur.aksesSahabat(s3, s4);
	
	return 0;
	
}