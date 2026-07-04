#include <stdio.h>

int main()
{
    float nota;

    printf("Qual sua nota: ");
    scanf("%f", &nota);

    if (nota >= 9)
    {
        printf("Nota: %f", nota);
        printf("Excelente");
    }

    else if (nota >= 7 && nota <= 8.9)
    {
        printf("Nota: %f", nota);
        printf("Aprovado");
    }

    else if (nota >= 5 && nota <= 6.9)
    {
        printf("Nota: %f", nota);
        printf("Recuperação");
    }

    else
    {
        printf("Nota: %f", nota);
        printf("Reprovado");
    }

    return 0;
}