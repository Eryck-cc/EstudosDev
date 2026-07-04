#include <stdio.h>

int main()
{
    float nota;

    printf("Digite sua nota: ");
    scanf("%f", &nota);

    if (nota >= 7)
    {
        printf("Aprovado!");
    }
    
    else
    {
        printf("Reprovado!");
    }

    return 0;
}