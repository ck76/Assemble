//
// Created by 程坤 on 2019-11-23.
//

#ifndef C_BOX_H
#define C_BOX_H

#include <iostream>

using namespace std;

class StaticBox {
public:
    static int objectCount;

    // 构造函数定义
    StaticBox(double l = 2.0, double b = 2.0, double h = 2.0);

    double Volume();

    static int getCount();

private:
    double length;     // 长度
    double breadth;    // 宽度
    double height;     // 高度
};

// 初始化类 StaticBox 的静态成员
int StaticBox::objectCount = 0;


#endif //C_BOX_H
