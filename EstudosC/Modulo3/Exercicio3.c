#include <stdio.h>

int main()
{
    int num;
    int contagem = 0;

    printf("Digite um número inteiro: ");
    scanf("%d", &num);

    while (contagem != num)
    {
        printf("%d", contagem);
        contagem ++;
    }
    return 0;
}