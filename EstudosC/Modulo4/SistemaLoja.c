#include <stdio.h>

int main()
{
    int opcao;
    float preco;
    int quantidade;
    float total_compra;
    int desconto;
    
    do
    {
        printf("=========================\n        Loja Dev\n=========================\n");
        printf("1 - Compra do Produto\n2 - Ver Total de Compra\n3 - Aplicar Desconto\n4 - Finalizar Compra\n0 - Fechar Caixar\n");
        printf("\nEscolha: ");
        scanf("%d", &opcao);

        switch (opcao)
    {
        case 0:
        printf("Fechando caixa!");
        break;

        case 1:
        printf("Nome do Produto: \n");//Simulação
        printf("Preço: ");
        scanf("%f", &preco);
        printf("Quantidade: ");
        scanf("%d", &quantidade);
        total_compra = preco * quantidade;
        break;

        case 2:
        printf("R$%d", total_compra);
        break;

        case 3:
        printf("Digite a quantidade de desconto: ");
        scanf("%d", &desconto);

        if (desconto <= 0 || desconto >= 100)
        {
            printf("Não é possivel colocar 0 ou 100 porcento de desconto!");
            break;
        }
        else
        {
            desconto = desconto / 100;
            total_compra = total_compra - (total_compra * desconto);
            break;
        }

        case 4:
        printf("Compra finalizada\nTotal da compra: %.2f", total_compra);
        break;
        



    }

    } 
    while (opcao > 0 || opcao < 0);



    




    return 0;
}