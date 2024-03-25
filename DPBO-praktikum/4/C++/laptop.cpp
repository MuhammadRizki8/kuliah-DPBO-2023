#include "header.hh"

// konstruktor
Laptop::Laptop()
{
    brand = "";
    speedMHz = 0;
}

// konstruktor
Laptop::Laptop(string brand, int speedMHz)
{
    this->brand = brand;
    this->speedMHz = speedMHz;
}

// getter dan setter
string Laptop::getBrand()
{
    return brand;
}

void Laptop::setBrand(string brand)
{
    this->brand = brand;
}

int Laptop::getSpeedMHz()
{
    return speedMHz;
}

void Laptop::setSpeedMHz(int speedMHz)
{
    this->speedMHz = speedMHz;
}

// destruktor
Laptop::~Laptop()
{
}