#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(int argc ,char *argv[]){
  unsigned char c[] = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽";
  int i =0;
  while (i  < sizeof(c))
  {
    c[i] = c[i]>>8;
    c[i] -=1;
 
  printf("%c",c[i]);  
   i++;
  }



  
  
   
    
  }
  




    

