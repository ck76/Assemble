//
// Created by 程坤 on 2019-11-20.
//

#include <iostream>
#include "Box.h"
#include <iostream>

using namespace std;

using namespace std;

double length;      // 长度
double breadth;     // 宽度
double height;      // 高度

//类的外部使用范围解析运算符 :: 定义该函数
//:: 叫作用域区分符，指明一个函数属于哪个类或一个数据属于哪个类。
//:: 可以不跟类名，表示全局数据或全局函数（即非成员函数）。
double Math::getVolume() {
    return length * breadth * height;;
}

void Math::externFun() {
    std::cout << "externFun";
}

void Math::leidechengyuanhanshu() {
    //【1】类的成员函数
    Math mBox;
    mBox.breadth = 10;
    mBox.height = 10;
    mBox.length = 10;
    std::cout << mBox.getVolume() << std::endl;
    mBox.externFun();

    std::cout << "--------" << endl;
    Circle circle = Circle(100);
    std::cout << circle.mianji() << endl;
}