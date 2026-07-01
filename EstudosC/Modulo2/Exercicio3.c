#include <stdio.h>

int main()
{
    char inicial = 'E';
    int idade = 20;
    float altura = 1.70;
    double peso = 70.5;

    printf("Char ocupa %zu byte(s)\n", sizeof(inicial));
    printf("Int ocupa %zu byte(s)\n", sizeof(idade));
    printf("Float ocupa %zu byte(s)\n", sizeof(altura));
    printf("Double ocupa %zu byte(s)\n", sizeof(peso));

    return 0;
}