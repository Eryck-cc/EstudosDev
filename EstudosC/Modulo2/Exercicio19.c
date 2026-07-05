#include <stdio.h>

int main()
{
    int opcao;

    printf("[1] - Novo Jogo\n[2] - Carregar Jogo\n[3] - Configurações\n[4] - Sair\nDigite sua opção: ");
    scanf("%d", &opcao);

    switch (opcao)
    {
        case 1:
        printf("Carregando novo jogo");
        break;

        case 2:
        printf("Carregando jogo");
        break;

        case 3:
        printf("Abrindo configurações");
        break;

        case 4:
        printf("Saindo");
        break;

        default:
        printf("Número invalido");
    }
    
    return 0;

}