#include <iostream>
#include <string>
using namespace std;

class Profession
{
	private:
		string position;
		int salaryPerMonth;
	
	public:
		Profession();
		Profession(string position, int salaryPerMonth);
		
		string getPosition();
		void setPosition(string position);
		int getSalaryPerMonth();
		void setSalaryPerMonth(int salaryPerMonth);
		
		~Profession();
};

class Laptop
{
	private:
		string brand;
		int speedMHz;
	
	public:
		Laptop();
		Laptop(string brand, int speedMHz);
		
		string getBrand();
		void setBrand(string brand);
		int getSpeedMHz();
		void setSpeedMHz(int speedMHz);
		
		~Laptop();
};

class Human
{
	private:
		string name;
		char gender;
	
	public:
		Human();
		Human(string name, char gender);
		
		string getName();
		void setName(string name);
		char getGender();
		void setGender(char gender);
		
		~Human();
};

class Adult : public Human
{
	private:
		Profession profession;
		Laptop laptop;
		
	public:
		Adult();
		Adult(string name, char gender);
		Adult(string name, char gender, Profession profession, Laptop laptop);
		
		Profession getProfession();
		void setProfession(Profession profession);
		Laptop getLaptop();
		void setLaptop(Laptop laptop);
		
		~Adult();
};