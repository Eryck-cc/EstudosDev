#include <stdio.h>

int main()
{
    int idade;

    printf("Digite sua idade: ");
    scanf("%d", &idade);

    printf("Maior idade? %d\n", idade >= 18);

    return 0;
}