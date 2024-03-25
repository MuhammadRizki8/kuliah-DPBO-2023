class Titik3D : public Titik{
	private:
		int z;
	
	public:
		Titik3D(){
			z = 0;
		}
		Titik3D(int xp, int yp, int zp){
			setX(xp);
			setY(yp);
			z = zp;
		}
		friend void tampilkanTitik(Titik t1, Titik3D t2);
		
	protected:
		int getZ(){
			return z;
		}
		void setZ(int zp){
			z = zp;
		}
};