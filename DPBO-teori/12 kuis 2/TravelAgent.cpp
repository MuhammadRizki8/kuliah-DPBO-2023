class TravelAgent {
private:
    string m_name;
    string m_address;
    string m_phone;
    string m_email;
    vector<Tour> m_tours;
    friend class Customer;
public:
    TravelAgent(){

    }
    TravelAgent(string name, string address, string phone, string email){
        m_name=name;
        m_address=address;
        m_phone=phone;
        m_email=email; 
    }
    // Getter untuk nama
    string getName()  {
        return m_name;
    }

    // Setter untuk alamat
    void setAddress( string& address) {
        m_address = address;
    }

    // Getter untuk alamat
    string getAddress()  {
        return m_address;
    }

    // Setter untuk nomor telepon
    void setPhone( string& phone) {
        m_phone = phone;
    }

    // Getter untuk nomor telepon
    string getPhone()  {
        return m_phone;
    }

    // Setter untuk email
    void setEmail( string& email) {
        m_email = email;
    }

    // Getter untuk email
    string getEmail(){
        return m_email;
    }

    // Method untuk menambahkan tour ke dalam daftar tour yang tersedia
    void addTour(Tour& tour) {
        m_tours.push_back(tour);
    }

    // Method untuk menampilkan daftar tour yang tersedia
    void displayTours() {
        cout << "Tour yang tersedia:" << endl;
        for (const auto& tour : m_tours) {
            tour.display();
            cout << endl;
        }
    }

    // Method untuk membantu customer memesan tour
    void bookTour(const Tour& tour, Customer& customer) {
        cout << "Booking tour untuk customer: " << customer.getName() << endl;
        cout << "Detail:" << endl;
        tour.display();

        cout << endl;
        // Method untuk mengatur detail perjalanan seperti tiket, akomodasi, dan transportasi dapat ditambahkan di sini
    }
    ~TravelAgent(){
        
    }
};
