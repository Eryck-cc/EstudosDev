#include <stdio.h>

int main()
{
    int idade;
    float altura;
    char inicial;

    printf("Digite sua idade: \n");
    scanf("%d", &idade);

    printf("Digite sua altura: \n");
    scanf("%.2f", &altura);

    printf("Digite a inicial do seu nome: ");
    scanf(" %c", &inicial);

    printf(
        "Sua idade é: %d\n"
        "Sua altura é: %f\n"
        "Sua inicial é: %c",
        idade,
        altura,
        inicial
);    

    return 0;
}