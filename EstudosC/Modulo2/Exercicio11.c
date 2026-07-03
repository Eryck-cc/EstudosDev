#include <stdio.h>

int main()
{
    int idade;
    float nota;

    printf("Digite sua idade: ");
    scanf("%d", &idade);

    printf("Digite sua nota: ");
    scanf("%f", &nota);

    printf("Pode entrar?\n");
    printf("%d", idade >= 18 && nota >= 7);


    return 0;
}