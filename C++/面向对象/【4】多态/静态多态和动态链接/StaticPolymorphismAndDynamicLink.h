//
// Created by 程坤 on 2019-11-24.
//

#ifndef C_STATICPOLYMORPHISMANDDYNAMICLINK_H
#define C_STATICPOLYMORPHISMANDDYNAMICLINK_H


#include <iostream>

using namespace std;

class StaticShape {
protected:
    int width, height;
public:
    StaticShape(int a = 0, int b = 0) {
        width = a;
        height = b;
    }

    int area() {
        cout << "Parent class area :" << endl;
        return 0;
    }
};

class StaticRectangle : public StaticShape {
public:
    StaticRectangle(int a = 0, int b = 0) : StaticShape(a, b) {}

    int area() {
        cout << "Rectangle class area :" << endl;
        return (width * height);
    }
};

class StaticTriangle : public StaticShape {
public:
    StaticTriangle(int a = 0, int b = 0) : StaticShape(a, b) {}

    int area() {
        cout << "Triangle class area :" << endl;
        return (width * height / 2);
    }
};

////////////////////////////////////////////////
class DynamicShape {
protected:
    int width, height;
public:
    DynamicShape(int a = 0, int b = 0) {
        width = a;
        height = b;
    }

    //
    virtual int area() {
        cout << "Parent class area :" << endl;
        return 0;
    }
};

class DynamicRectangle : public DynamicShape {
public:
    DynamicRectangle(int a = 0, int b = 0) : DynamicShape(a, b) {}

    int area() {
        cout << "Rectangle class area :" << endl;
        return (width * height);
    }
};

class DynamicTriangle : public DynamicShape {
public:
    DynamicTriangle(int a = 0, int b = 0) : DynamicShape(a, b) {}

    int area() {
        cout << "Triangle class area :" << endl;
        return (width * height / 2);
    }
};



class StaticPolymorphismAndDynamicLink{
public:
    void jingtaiduotai();

    void dongtailianjie();

};
#endif //C_STATICPOLYMORPHISMANDDYNAMICLINK_H
