#include <stdio.h>

int main()
{
    float saldo = 1000.00;
    int escolha;
    float deposito;
    float sacar;
    float transferir;
    int operacoes = 0;

    do
    {
        printf("1 - Consultar Saldo\n2 - Depositar\n3 - Sacar\n4 - Transferir\n0 - Sair\n\nEscolha: ");
        scanf("%d", &escolha);

        switch (escolha)
        {
            case 1:
            printf("Seu saldo é : R$%.2f\n", saldo);
            break;

            case 2:
            printf("Digite quanto deseja depositar: ");
            scanf("%f", &deposito);
            if (deposito <= 0)
            {
                printf("Não é aceito valores negativos ou igual a zero\n");
                break;
            }
            else
            {
                printf("Saldo atualizado!\n");
                saldo = saldo + deposito;
                operacoes ++;
                break;
            }

            case 3:
            printf("Quanto deseja sacar: ");
            scanf("%f", &sacar);
            if (sacar <= 0 || sacar > saldo)
            {
                printf("Não é permitido sacar um valor menor que zero ou maior que o saldo\n");
                break;
            }
            else
            {
                printf("Saque realizado com sucesso\n");
                saldo = saldo - sacar;
                operacoes ++;
                break;
            }
            
            case 4:
            printf("Digite o valor que deseja transferir: \n");
            scanf("%f", &transferir);
            if (transferir <= 0 || transferir > saldo)
            {
                printf("Não é possivel transferir um valor menor que 0 ou maior que o saldo!\n");
                break;
            }
            else
            {
                printf("Tranferencia realizada com sucesso\n");
                saldo = saldo - transferir;
                operacoes ++;
                break;
            }

            default:
            {
                printf("Opção incorreta");
                break;
            }
        }

    }
    while (escolha != 0);
    
    printf("Foram realizadas %d operações\n", operacoes);
    printf("Seu saldo ficou %.2f\n", saldo);
    printf("Encerrando programa");

    return 0;
}