//
// Created by 程坤 on 2019-11-24.
//

#include "StaticPolymorphismAndDynamicLink.h"

void StaticPolymorphismAndDynamicLink::jingtaiduotai() {
    cout << "###############     多态    ##########" << endl;
    StaticShape *shape;
    StaticRectangle rec(10, 7);
    StaticTriangle tri(10, 5);

    // 存储矩形的地址
    shape = &rec;
    // 调用矩形的求面积函数 area
    shape->area();

    // 存储三角形的地址
    shape = &tri;
    // 调用三角形的求面积函数 area
    shape->area();
}

void StaticPolymorphismAndDynamicLink::dongtailianjie() {
    cout << "###############     动态链接    ##########" << endl;
    DynamicShape *shape;
    DynamicRectangle rec(10, 7);
    DynamicTriangle tri(10, 5);

    // 存储矩形的地址
    shape = &rec;
    // 调用矩形的求面积函数 area
    shape->area();

    // 存储三角形的地址
    shape = &tri;
    // 调用三角形的求面积函数 area
    shape->area();
}

