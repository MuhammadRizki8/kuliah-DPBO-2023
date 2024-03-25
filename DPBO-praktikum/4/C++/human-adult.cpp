#include "header.hh"

/* == HUMAN SECTION = = */

/* Constructor. */

// Empty constructor.
Human::Human(){
    name = "";
    gender = '-';
}

// Constructor with all atributes.
Human::Human(string name, char gender){
    this->name = name;
    this->gender = gender;
}

/* Getter and Setter. */
string Human::getName(){
    return name;
}

void Human::setName(string name){
    this->name = name;
}

char Human::getGender(){
    return gender;
}

void Human::setGender(char gender){
    this->gender = gender;
}

/* Destructor. */

// Leave it blank
Human::~Human(){

}

/* == ADULT SECTION = = */

/* Constructor. */

// Empty constructor
Adult::Adult() : Human(){

}

// Constructor with base human attribute.
Adult::Adult(string name, char gender) : Human(name, gender){

}

// Constructor with all attributes
Adult::Adult(string name, char gender, Profession profession, Laptop laptop) :
    Human(name, gender){
    this->profession = profession;
    this->laptop = laptop;
}

/* Getter and Setter. */

Profession Adult::getProfession(){
    return profession;
}

void Adult::setProfession(Profession profession){
    this->profession = profession;
}

Laptop Adult::getLaptop(){
    return laptop;
}

void Adult::setLaptop(Laptop laptop){
    this->laptop = laptop;
}

/* Destructor. */

// Leave it blank for now.
Adult::~Adult(){

}