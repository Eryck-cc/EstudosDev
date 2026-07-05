#include <stdio.h>

int main()
{
    int senha = 1234;
    int senhauser;

    while (senhauser != senha)
    {
        printf("Digite sua senha: ");
        scanf("%d", &senhauser);

        if (senhauser != senha)
        {
            printf("Senha incorreta\n");
        }
        else
        {
            printf("Senha correta");
        }
    }

    return 0;
}