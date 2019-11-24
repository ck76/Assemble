//
// Created by 程坤 on 2019-11-23.
//

#include "MySelf.h"
#include "Friend.h"
#include "iostream"
#include <string>


using namespace std;

void printMySelf(MySelf mySelf) {
    cout << "我是友元函数"<<endl;
    cout << mySelf.id << endl;
}

void MySelf::printMySelfClass() {
    cout << "我是友元类调用的函数"<<endl;
}

MySelf::MySelf(int id):id(id) {

}

MySelf::MySelf() {

}

void MySelf::youyuanhanshu() {

    //【3】友元函数
    MySelf mySelf = MySelf(19980804);
    printMySelf(mySelf);
    Friend aFriend;

    MySelf mySelf1;
    MySelf *mySelf2 = new MySelf();
    aFriend.printFriendsFun(mySelf1, mySelf2);
}
