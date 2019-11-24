//
// Created by 程坤 on 2019-11-20.
//

#ifndef C_BOX_H
#define C_BOX_H


class Math {
public:
    double length;      // 长度
    double breadth;     // 宽度
    double height;      // 高度
    double getVolume();

    void externFun();

    void leidechengyuanhanshu();

};

class Circle {
    //可以由多个public等
public:
    Circle(double r);

    double r;

    double mianji();

public:
    double publicDouble;
};

#endif //C_BOX_H
