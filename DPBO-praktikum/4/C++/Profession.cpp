#include "header.hh"

Profession::Profession()
{
	position ="";
	salaryPerMonth = 0;
}

Profession::Profession(string position, int salaryPerMonth)
{
	this->position = position;
	this->salaryPerMonth = salaryPerMonth;
}

string Profession::getPosition(){
	return position;
}

void Profession::setPosition(string position){
	this->position = position;
}

int Profession::getSalaryPerMonth(){
	return salaryPerMonth;
}

void Profession::setSalaryPerMonth(int salaryPerMonth){
	this->salaryPerMonth = salaryPerMonth;
}

Profession::~Profession(){
	
}