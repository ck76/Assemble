//
// Created by 程坤 on 2019-11-23.
//

#ifndef C_DEMO_H
#define C_DEMO_H
#include <string>
#include <iostream>

class Constructor{
public:
    Constructor(){}
    Constructor(int s);

    ~Constructor();
    void gouzaoshanshuhexigouhanshu();

private:
    int m_s;
};

void constructorFunc();




#endif //C_DEMO_H
