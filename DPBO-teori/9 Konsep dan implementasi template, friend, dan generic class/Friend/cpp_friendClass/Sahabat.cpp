class TemannyaSahabat;
class Sahabat{
	private:
		int atributSahabat;
		
	public:
		Sahabat(){
			atributSahabat = 89;
		}
		friend class TemannyaSahabat;
};