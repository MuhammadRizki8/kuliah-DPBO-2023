#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
#include "Tour.cpp"
#include "Customer.cpp"
#include "TravelAgent.cpp"

int main() {
    // Membuat objek TravelAgent
    TravelAgent travelAgent("Travel Rizki", "Jalan Dt.Mustofa No.7", "+6283164919553", "travelRizki@gmail.com");

    // Menambahkan tour ke dalam daftar tour yang tersedia
    Tour tour1("Bali Adventure", "Explore Keindahan pantai Bali nan Eksotik", 1200, "2023-06-15", 7, "Bali");
    Tour tour2("Java Explorer", "Pengalaman menjelajahin tanah jawa dengan kearagaman budayanya", 1500, "2023-07-10", 10, "Java");
    travelAgent.addTour(tour1);
    travelAgent.addTour(tour2);

    // Menampilkan daftar tour yang tersedia
    travelAgent.displayTours();

    // Membuat objek Customer
    Customer customer("Robert Sanusi", "Jalan jalan entah kemana No. 10", "+6289876543210");

    // Customer memesan tour
    cout << "Customer " << customer.getName() << " books tour:" << endl;
    customer.bookTour(travelAgent, tour1);
    cout<<"---------------------\n";
    customer.bookTour(travelAgent,tour2);
    customer.displayHistoryTours();


    return 0;
}
