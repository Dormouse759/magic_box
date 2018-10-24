#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

    int main(void){
    double latency;
    double correction;

    srand(time(0));

    do{
        latency = (rand()%1000+15000)+(rand()%1000)/100;
        correction = (rand()%10000)/100;
        fprintf(stdout, "2 %lu %.3f %.3f\n",(unsigned long)time(NULL), latency, correction);
	sleep(1);
    }while(1); 
}
