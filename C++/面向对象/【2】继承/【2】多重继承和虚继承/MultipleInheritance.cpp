//
// Created by 程坤 on 2019-11-24.
//

//间接基类A
class A {
protected:
    int m_a;
};

//直接基类B
class B : public A {
protected:
    int m_b;
};

//直接基类C
class C : public A {
protected:
    int m_c;
};

//派生类D
class D : public B, public C {
public:
    /**
     * 这段代码实现了上图所示的菱形继承，第 25 行代码试图直接访问成员变量 m_a，
     * 结果发生了错误，因为类 B 和类 C 中都有成员变量 m_a（从 A 类继承而来），
     * 编译器不知道选用哪一个，所以产生了歧义。
     */
//    void seta(int a){ m_a = a; }  //命名冲突
    void setaB(int a) { B::m_a = a; }

    void setaC(int a) { C::m_a = a; }

    void setb(int b) { m_b = b; }  //正确
    void setc(int c) { m_c = c; }  //正确
    void setd(int d) { m_d = d; }  //正确
private:
    int m_d;
};

int duochongjicheng() {
    D d;
    return 0;
}

/**
在一个派生类中保留间接基类的多份同名成员，
 虽然可以在不同的成员变量中分别存放不同的数据，
 但大多数情况下这是多余的：因为保留多份成员变量不仅占用较多的存储空间，还容易产生命名冲突。
 假如类 A 有一个成员变量 a，那么在类 D 中直接访问 a 就会产生歧义，
 编译器不知道它究竟来自 A -->B-->D 这条路径，还是来自 A-->C-->D 这条路径。
 **/