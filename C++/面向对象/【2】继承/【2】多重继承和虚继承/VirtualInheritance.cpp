//
// Created by 程坤 on 2019-11-24.
//

//间接基类A
class A {
public:
    int x;
protected:
    int m_a;
};

//直接基类B
class B : virtual public A {  //虚继承
public:
    int x;
protected:
    int m_b;
};

//直接基类C
class C : virtual public A {  //虚继承
public:
    int x;
protected:
    int m_c;
};

//派生类D
class D : public B, public C {
public:
    void seta(int a) { m_a = a; }  //正确
    void setb(int b) { m_b = b; }  //正确
    void setc(int c) { m_c = c; }  //正确
    void setd(int d) { m_d = d; }  //正确
private:
    int m_d;
};

int xujicheng() {
    D d;
    //虚基类成员的可见性
    /**
     * - 因为在虚继承的最终派生类中只保留了一份虚基类的成员，所以该成员可以被直接访问，不会产生二义性。
     * 此外，如果虚基类的成员只被一条派生路径覆盖，那么仍然可以直接访问这个被覆盖的成员。但是如果该成员被两条或多条路径覆盖了，那就不能直接访问了，此时必须指明该成员属于哪个类。
        - 假设 A 定义了一个名为 x 的成员变量，当我们在 D 中直接访问 x 时，会有三种可能性：
          - 如果 B 和 C 中都没有 x 的定义，那么 x 将被解析为 B 的成员，此时不存在二义性。
          - 如果 B 或 C 其中的一个类定义了 x，也不会有二义性，派生类的 x 比虚基类的 x 优先级更高。
          - 如果 B 和 C 中都定义了 x，那么直接访问 x 将产生二义性问题。
     */
//    d.x;
    return 0;
}

/*
 *
虚继承的目的是让某个类做出声明，承诺愿意共享它的基类。
 其中，这个被共享的基类就称为虚基类（Virtual Base Class），
 本例中的 A 就是一个虚基类。在这种机制下，不论虚基类在继承体系中出现了多少次，
 在派生类中都只包含一份虚基类的成员。
 */