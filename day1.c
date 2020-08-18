#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int N;
    int d;
    scanf("%d %d", &N, &d);  
    int A[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);    
    }
    for (int i = 0; i < N; i++)
    {
        printf("%d ", A[(i + d) % N]);    
    }
    puts("");
    
    return 0;
}