#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int main(){
unsigned char txt[]="gvswwmrkxlivyfmgsrhnrisegl";
int a =1;
int i =0;
while (a<27){
while(i<sizeof(txt)){
    txt[i] += 9;
    if (txt[i]>'z')
        txt[i]= txt[i]-'z'+'a';
    printf("%c ",txt[i]);
    printf("\n");
    i++;
}
a++;
}
}
