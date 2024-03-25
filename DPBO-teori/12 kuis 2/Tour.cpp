class Tour {
private:
    string m_name;
    string m_description;
    double m_price;
    string m_departureDate;
    int m_duration;
    string m_destination;
    friend class TravelAgent;
public:
    Tour(){

    }
    Tour(const string& name, const string& description, double price, const string& departureDate, int duration, const string& destination){
        m_name=name;
        m_description=description;
        m_price=price;
        m_departureDate=departureDate;
        m_duration=duration;
        m_destination=destination;
    }
    string getName() {
        return m_name;
    }
    string getDescription() {
        return m_description;
    }
    string getDepartureDate() {
        return m_departureDate;
    }
    string getDestination() {
        return m_destination;
    }
    double getPrice(){
        return m_price;
    }
    int getDuration(){
        return m_duration;
    }
    void setName(const string& name){
        m_name = name;
    }

    void setDescription(const string& description){
        m_description = description;
    }

    void setDepartureDate(const string& departureDate){
        m_departureDate = departureDate;
    }

    void setDestination(const string& destination){
        m_destination = destination;
    }

    void setPrice(double price){
        m_price = price;
    }

    void setDuration(int duration){
        m_duration = duration;
    }

    // Method untuk menampilkan detail tour
    void display() const {
        cout << "Nama Tour: " << m_name << endl;
        cout << "Deskripsi: " << m_description << endl;
        cout << "Harga: $" << m_price << endl;
        cout << "Tanggal Keberangkatan: " << m_departureDate << endl;
        cout << "Durasi: " << m_duration << " hari" << endl;
        cout << "Destinasi: " << m_destination << endl;
    }
    ~Tour(){

    }
};