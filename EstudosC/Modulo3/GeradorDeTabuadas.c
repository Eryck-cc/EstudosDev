#include <stdio.h>

int main()
{
    int numero;
    int opcao;

    do
    {
        printf("Digite um número: ");
        scanf("%d", &numero);

        for (int vezes = 1; vezes <= 10; vezes ++ )
    {
        printf("%d x %d = %d\n", numero, vezes, numero * vezes);

    }

        printf("Deseja gera outra tabuada? [1] - Sim, [2] - Não >");
        scanf("%d", &opcao);
    }

    while (opcao == 1);
    

    
    return 0;
}
