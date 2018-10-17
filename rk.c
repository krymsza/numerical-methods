#include<stdio.h>

double r_k(){
    double dex = 2;
    double s = 2;
    double a21;
    double y0 = 1.0;
    double k1 = y0;
    double k2 = y0 + 0.5*dex*k1;
    double c2 = a21 = 0.5;
    double y1=1, b1 = 1, b2 =1, temp;
    k2=2;y0=1;
    printf("%f %f\n",0,1);
    for(double x=dex; x<=s; x+=dex){
        y0=y1;
        y1 = y0 + dex*(b1*k1 +b2*k2);
        printf("%f %f\n",x,y1);
        k2 = y0 + 0.5*dex*k1;
        y0=y1;
    }
}


int main(){
    r_k();
}
