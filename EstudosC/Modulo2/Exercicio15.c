#include <stdio.h>

int main()
{
    int idade;
    float nota;

    printf("Qual sua idade: ");
    scanf("%d", &idade);

    printf("Qual sua nota: ");
    scanf("%f", &nota);

    if (idade >= 18 && nota >= 7)
    {
        printf("Aprovado!");
    }

    else
    {
        printf("Reprovado!");
    }

    return 0;
}