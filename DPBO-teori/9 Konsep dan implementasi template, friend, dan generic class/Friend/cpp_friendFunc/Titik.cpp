class Titik3D;
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
		friend void tampilkanTitik(Titik t1, Titik3D t2);
		
};