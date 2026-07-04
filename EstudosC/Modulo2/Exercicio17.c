#include <stdio.h>

int main()
{
    int idade;

    printf("Qual sua idade: ");
    scanf("%d", &idade);

    if (idade >= 60)
    {
        printf("Idoso");
    }

    else if (idade >= 18 && idade <= 59)
    {
        printf("Adulto");
    }

    else if (idade >= 13 && idade <= 17)
    {
        printf("Adolescente");
    }

    else
    {
        printf("Criança");
    }

    return 0;
}