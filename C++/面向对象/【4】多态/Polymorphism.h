//
// Created by 程坤 on 2019-11-24.
//

#ifndef C_POLYMORPHISM_H
#define C_POLYMORPHISM_H

#include <iostream>

using namespace std;

//为什么定义和声明放在。h中会报错
//头文件可能被多个文件include，所以只可以写函数的声明，不可以定义函数实体，
// 如果这个头文件只有一个源文件包含也不会报错，但是也是不推荐的

//http://c.biancheng.net/view/2284.html
//基类
class PolymorphismA {
public:
    PolymorphismA(int a);

public:
    void display();

public:
    int m_a;
};


//派生类
class PolymorphismB : public PolymorphismA {
public:
    PolymorphismB(int a, int b);

    void display();

public:
    int m_b;
};


class Polymorphism {
public:
    void duotai();
};


#endif //C_POLYMORPHISM_H
