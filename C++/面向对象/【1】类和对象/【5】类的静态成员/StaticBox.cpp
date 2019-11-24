//
// Created by 程坤 on 2019-11-23.
//

#include "StaticBox.h"

StaticBox::StaticBox(double l, double b, double h) {
    cout << "Constructor called." << endl;
    length = l;
    breadth = b;
    height = h;
    // 每次创建对象时增加 1
    objectCount++;
}

double StaticBox::Volume() {
    return length * breadth * height;
}

int StaticBox::getCount() {
    return objectCount;
}