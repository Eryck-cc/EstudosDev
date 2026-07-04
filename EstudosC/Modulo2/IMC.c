#include <stdio.h>

int main()
{
    int peso;
    float altura;

    printf("Digite seu peso: ");
    scanf("%d", &peso);

    printf("Digite sua altura: ");
    scanf("%f", &altura);

    float imc = (float) peso / (altura * altura);

    if (imc >= 30)
    {
        printf("Obesidade");
    }

    else if (imc >= 25 && imc <= 29.9)
    {
        printf("Sobrepeso");
    }

    else if (imc >= 18.5 && imc <= 24.9)
    {
        printf("Peso normal");
    }

    else
    {
        printf("Abaixo do peso");
    }

    return 0;
}