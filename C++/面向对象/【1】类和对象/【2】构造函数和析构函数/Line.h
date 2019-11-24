//
// Created by 程坤 on 2019-11-23.
//

#ifndef C_LINE_H
#define C_LINE_H


class Line {
public:
    int getLength(void);

    explicit Line(int len);             // 简单的构造函数
    Line(const Line &obj);      // 拷贝构造函数
    ~Line();                     // 析构函数

private:
    int *ptr;
};

void display(Line obj);

#endif //C_LINE_H
