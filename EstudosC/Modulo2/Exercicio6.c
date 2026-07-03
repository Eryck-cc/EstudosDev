#include <stdio.h>

int main()
{
    int num1;
    int num2;

    printf("Digite o primeiro número: ");
    scanf("%d", &num1);

    printf("Digite o segundo número: ");
    scanf("%d", &num2);

    printf("Soma = %d\n", num1 + num2);
    printf("Subtração = %d\n", num1 - num2);
    printf("Multiplicação = %d\n", num1 * num2);
    printf("Divisão inteira = %d\n", num1 / num2);
    printf("Resto da divisão = %d\n", num1 % num2);
    printf("A média = %.2f", (num1 + num2)/2.0);

    return 0;
}