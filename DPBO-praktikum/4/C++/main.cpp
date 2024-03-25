#include "header.hh"

int main()
{
    Laptop laptop("ASUS", 3200);
    Profession profession("Programmer", 1000000);

    Adult adult("Rain", 'L', profession, laptop);

    // print
    cout << "Name : " << adult.getName() << '\n';
    cout << "Gender : " << adult.getGender() << "\n\n";
    cout << adult.getName() << "'s job is : " << adult.getProfession().getPosition() << '\n';
    cout << adult.getName() << "'s salary per year is  : " << (adult.getProfession().getSalaryPerMonth() * 12) << '\n';
    cout << adult.getName() << "'s laptop and its speed is : " << adult.getLaptop().getBrand() << "-" << adult.getLaptop().getSpeedMHz() << '\n';
    return 0;
}