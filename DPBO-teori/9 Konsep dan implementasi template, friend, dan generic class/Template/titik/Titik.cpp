#include "Titik.h"
template <class T>
Titik<T>:: Titik () {
    /*konstruktor*/
    Titik<T>::x = 0;
    Titik<T>:: y = 0;
}
template <class T>
Titik<T>:: Titik (T xp, T yp) {
/*konstruktor*/
Titik<T>::x = xp;
Titik<T>::y = yp;
}

template <class T>
T Titik<T>::getX(){
    return Titik<T>::x;
}

template <class T>
T Titik<T>::getY(){
    return Titik<T>::y;
}

template <class T>
void Titik<T>::setX(T xp){
    Titik<T>::x=xp;
}

template <class T>
void Titik<T>::setY(T yp){
    Titik<T>::y=yp;
}

template<class T>
Titik<T>::~Titik(){}