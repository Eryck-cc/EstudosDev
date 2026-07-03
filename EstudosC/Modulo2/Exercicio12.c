#include <stdio.h>

int main()
{
    int idade;
    float nota;

    printf("Digite sua idade: ");
    scanf("%d", &idade);

    printf("Digite sua nota: ");
    scanf("%f", &nota);

    printf("Maior de idade e aprovado?\n");
    printf("%d", idade >= 18 && nota >= 7);
    
    printf("Maior de idade ou aprovado?\n");
    printf("%d", idade >= 18 || nota >= 7);

    printf("Não e maior de idade");
    printf("%d", !(idade >= 18));

    return 0;
}