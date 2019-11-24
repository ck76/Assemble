//
// Created by 程坤 on 2019-11-24.
//

#include "Polymorphism.h"

void Polymorphism::duotai() {
    cout << "###############     多态    ##########" << endl;
    PolymorphismA a(10);
    PolymorphismB b(66, 99);
    //赋值前
    a.display();
    b.display();
    cout << "--------------" << endl;
    //赋值后
    a = b;
    a.display();
    b.display();
}

void dongtailianjie() {
    cout << "###############     动态链接    ##########" << endl;
    PolymorphismA a(10);
    PolymorphismB b(66, 99);
    //赋值前
    a.display();
    b.display();
    cout << "--------------" << endl;
    //赋值后
    a = b;
    a.display();
    b.display();
}


PolymorphismB::PolymorphismB(int a, int b) : PolymorphismA(a), m_b(b) {}

void PolymorphismB::display() {
    cout << "Class B: m_a=" << m_a << ", m_b=" << m_b << endl;
}


PolymorphismA::PolymorphismA(int a) : m_a(a) {}

void PolymorphismA::display() {
    cout << "Class A: m_a=" << m_a << endl;
}
