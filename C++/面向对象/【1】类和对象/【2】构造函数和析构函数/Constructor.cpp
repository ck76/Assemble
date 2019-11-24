//
// Created by 程坤 on 2019-11-23.
//

#include "Constructor.h"
#include "Line.h"
#include <string>

#include <iostream>
using namespace std;


void constructorFunc() {
    //局部对象
    //函数执行完成之后就析构函数调用了
    Constructor obj1(1);
}

Constructor::Constructor(int s) : m_s(s) {}

Constructor::~Constructor() { cout << m_s << endl; }

void Constructor::gouzaoshanshuhexigouhanshu() {
    //【2】构造函数和析构函数
    //局部对象
    Constructor obj3(3);
    //new创建的对象
    auto *pobj4 = new Constructor(4); //始终没有释放
    constructorFunc();
    cout << "main" << endl;

    Line line1(10);
    Line line2 = line1; // 这里也调用了拷贝构造函数
    display(line1);
    display(line2);
}

//全局对象
Constructor obj2(2);