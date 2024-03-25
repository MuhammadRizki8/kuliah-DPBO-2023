class TravelAgent; // Forward declaration
class Tour;
class Customer {
private:

    string m_name;
    string m_address;
    string m_phone;
    vector<pair<string, string>> m_history;
public:
    Customer( string name,  string address,  string phone){
        m_name=name;
        m_address=address;
        m_phone=phone;
    }

    // Getter untuk nama
     string getName()  {
        return m_name;
    }

    // Setter untuk alamat
    void setAddress( string address) {
        m_address = address;
    }

    // Getter untuk alamat
     string getAddress()  {
        return m_address;
    }

    // Setter untuk nomor telepon
    void setPhone( string phone) {
        m_phone = phone;
    }

    // Getter untuk nomor telepon
     string getPhone()  {
        return m_phone;
    }

    // Method untuk memesan tour dari agen travel
    template<class T>
    void bookTour(T agent, Tour tour){
        agent.bookTour(tour, *this);
        addHistoryTour(agent.m_name,tour.getName());
    }

    // Method untuk menambahkan history tour
    void addHistoryTour(const string& tourName, const string& travelAgentName) {
        m_history.push_back(make_pair(tourName, travelAgentName));
    }


    // Method untuk menampilkan history tour customer
    void displayHistoryTours() {
        cout << "History tours dari customer " << m_name << ":" << endl;
        for (const auto& tour : m_history) {
            cout << "- Tour " << tour.first << " dengan travel agent " << tour.second << endl;
        }
    }
};