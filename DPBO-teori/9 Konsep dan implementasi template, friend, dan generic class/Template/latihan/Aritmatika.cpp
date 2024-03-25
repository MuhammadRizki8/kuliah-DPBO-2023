#include "Aritmatika.h"
template <class T>
Aritmatika<T>:: Aritmatika () {
    /*konstruktor*/
    Aritmatika<T>::x = 0;
    Aritmatika<T>:: y = 0;
}
template <class T>
Aritmatika<T>:: Aritmatika (T xp, T yp) {
/*konstruktor*/
Aritmatika<T>::x = xp;
Aritmatika<T>::y = yp;
}

template <class T>
T Aritmatika<T>::getX(){
    return Aritmatika<T>::x;
}

template <class T>
T Aritmatika<T>::getY(){
    return Aritmatika<T>::y;
}

template <class T>
void Aritmatika<T>::setX(T xp){
    Aritmatika<T>::x=xp;
}

template <class T>
void Aritmatika<T>::setY(T yp){
    Aritmatika<T>::y=yp;
}

template <class T>
T Aritmatika<T>::tambah(){
    return (this->x+this->y);
}
template <class T>
T Aritmatika<T>::kurang(){
    return (this->x-this->y);
}
template <class T>
T Aritmatika<T>::kali(){
    return (this->x*this->y);
}
template <class T>
T Aritmatika<T>::bagi(){
    return (this->x/this->y);
}

template<class T>
Aritmatika<T>::~Aritmatika(){}