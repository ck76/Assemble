//
// Created by 程坤 on 2019-11-23.
//

#ifndef C_MYSELF_H
#define C_MYSELF_H

#include <string>


class MySelf {
    int id;

public:
    explicit MySelf(int id);
    MySelf();
    friend void printMySelf(MySelf mySelf);

    friend class Friend;

    void youyuanhanshu();

private:
    void printMySelfClass();
};

#endif //C_MYSELF_H
