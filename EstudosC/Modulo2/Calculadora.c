#include <stdio.h>

int main()
{
    float num1;
    char operador;
    float num2;

    printf("Digite o primeiro número: ");
    scanf("%f", &num1);

    printf("Digite [+] para somar, [-] para subtrair, [*] para multiplicar e [/] para dividir: ");
    scanf(" %c", &operador);

    printf("Digite o segundo número: ");
    scanf("%f", &num2);

    switch (operador)
    {
        case '+':
        printf("[%f] + [%f] = [%.1f]", num1, num2, num1 + num2);
        break;

        case '-':
        printf("[%f] - [%f] = [%.1f]", num1, num2, num1 - num2);
        break;

        case '*':
        printf("[%f] x [%f] = [%.1f]", num1, num2, num1 * num2);
        break;

        case '/':
            if (num2 == 0)
            {
                printf("Não é possivel divisão por zero!");
            }

            else
            {
            printf("[%f] / [%f] = [%.1f]", num1, num2, num1 / num2);
            }
        break;

        default:
        printf("Opção invalida");
    }

    return 0;

}