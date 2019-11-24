//
// Created by 程坤 on 2019-11-20.
//

#ifndef C_BASE_H
#define C_BASE_H


class Base {

};

// 基类
class Shape : Base {
public:
    void setWidth(int w) {
        width = w;
    }

    void setHeight(int h) {
        height = h;
    }

protected:
    int width;
    int height;
};

// 派生类
class Rectangle : public Shape {
public:
    int getArea() {
        return (width * height);
    }
};


#endif //C_BASE_H
