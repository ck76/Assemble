//
// Created by 程坤 on 2019-11-20.
//

#include <cmath>

#include "Box.h"

double Circle::mianji() {
    return pow(r, 2) * 3.14;
}

Circle::Circle(double r) {
    this->r = r;
}

