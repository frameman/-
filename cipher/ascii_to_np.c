#include<stdio.h>
#include<stdlib.h>
#include<strings.h>

int main(){
int flag[] = {112 ,105 ,99 ,111 ,67 ,84 ,70 ,123 ,98 ,52 ,100 ,95 ,98 ,114 ,111 ,103 ,114 ,97 ,109 ,109 ,101 ,114 ,95 ,98 ,56 ,100 ,55 ,50 ,55 ,49 ,102 ,125};
unsigned p[50];
int j = sizeof(flag)/sizeof(flag[0]);
for (int i = 0 ; i<j;i++){
   p[i] = flag[i];
   printf("%C",p[i]);
}

}
