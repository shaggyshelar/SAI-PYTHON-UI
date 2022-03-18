#include<stdio.h>
#include "myhead.h"

int add_int(int, int);
int add_new(int, int);
float add_float(float, float);

int add_new(int num1, int num2){
    add(num1, num2);
}

int add_int(int num1, int num2){
    return num1 + num2;
}

float add_float(float num1, float num2){
    return num1 + num2;
}
