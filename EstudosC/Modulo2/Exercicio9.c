#include <stdio.h>

int main()
{
    int nota;

    printf("Digite sua nota: ");
    scanf("%d", &nota);

    printf("Nota maior ou igual a 7?\n");
    printf("%.d", nota >= 7);

    return 0;
}