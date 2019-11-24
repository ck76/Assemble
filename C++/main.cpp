#include <iostream>
#include "面向对象/【1】类和对象/【1】类的成员函数/Box.h"
#include "面向对象/【2】继承/【1】继承/Base.h"
#include "面向对象/【3】重载运算符和重载函数/重载函数/PrintData.h"
#include "面向对象/【1】类和对象/【2】构造函数和析构函数/Constructor.h"
#include "面向对象/【1】类和对象/【2】构造函数和析构函数/Line.h"
#include "面向对象/【1】类和对象/【3】友元函数/MySelf.h"
#include "面向对象/【1】类和对象/【3】友元函数/Friend.h"
#include "面向对象/【1】类和对象/【5】类的静态成员/StaticBox.h"
#include "面向对象/【4】多态/Polymorphism.h"
#include "面向对象/【4】多态/静态多态和动态链接/StaticPolymorphismAndDynamicLink.h"

using namespace std;

//【1】类和对象
void leiheduixiang() {
    cout << "################    类的成员函数    ##########" << endl;
    Math math;
    math.leidechengyuanhanshu();

    cout << "###############     构造函数和析构函数    ##########" << endl;
    Constructor constructor;
    constructor.gouzaoshanshuhexigouhanshu();

    cout << "###############     友元函数    ##########" << endl;
    MySelf mySelf;
    mySelf.youyuanhanshu();

    cout << "###############     类的静态成员    ##########" << endl;
    // 在创建对象之前输出对象的总数
//    cout << "Inital Stage Count: " << StaticBox::getCount() << endl;
//
//    StaticBox Box1(3.3, 1.2, 1.5);    // 声明 box1
//    StaticBox Box2(8.5, 6.0, 2.0);    // 声明 box2
//
//    // 在创建对象之后输出对象的总数
//    cout << "Final Stage Count: " << StaticBox::getCount() << endl;

}

void jicheng() {
    cout << "###############     重载函数    ##########" << endl;
    PrintData printData;
    printData.chongzaihanshu();
}

void duotai() {
    cout << "###############     多态    ##########" << endl;
    Polymorphism polymorphism;
    polymorphism.duotai();
    cout << "###############     静态多态和动态链接    ##########" << endl;
    StaticPolymorphismAndDynamicLink staticPolymorphismAndDynamicLink;
    staticPolymorphismAndDynamicLink.jingtaiduotai();
    staticPolymorphismAndDynamicLink.dongtailianjie();
}


int main() {
    leiheduixiang();
    jicheng();
    duotai();
    return 0;
}
