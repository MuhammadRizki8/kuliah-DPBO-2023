class Titik{
	private:
		int x;
		int y;
	
	public:
		Titik(){
			x = 0;
			y = 0;
		}
		Titik(int xp, int yp){
			x = xp;
			y = yp;
		}
		int getX(){
			return x;
		}
		void setX(int xp){
			x = xp;
		}
		int getY(){
			return y;
		}
		void setY(int yp){
			y = yp;
		}
		friend void SahabatTitik::printTitik(const Titik &t);		
};

void SahabatTitik::printTitik(const Titik &t){
	cout << "Metode Firend" << endl;
	cout << "Titik : x : " << t.x << " y : " << t.y << endl;
	cout << "-----------" << endl;
}