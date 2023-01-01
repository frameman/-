#include <stdio.h>
#include <stdlib.h>
#include<string.h>
int main(){
char q[]= "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}";
int i = 0;
while (i<sizeof(q)){
 if ((q[i]>=97 && q[i]<= 109) || (q[i]>=65 && q[i] <=77)){
     q[i] +=13;
 }
 else if ((q[i]>=110 && q[i] <=122)||(q[i]>=78 && q[i] <=90)){
     q[i] -=13;
 }
printf("%c",q[i]);
i++;
}
}
