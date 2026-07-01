/*Escreva um programa que declare:

nome (apenas a inicial)
idade
altura

Exemplo:

char inicial = 'E';
int idade = 22;
float altura = 1.75;

Depois imprima exatamente:

Inicial: E
Idade: 22
Altura: 1.75*/

#include <stdio.h>

int main(){

    char nome = 'E';
    int idade = 20;
    float altura = 1.70;

    printf("Inicial: %c\nIdade: %d\nAltura: %.2f",
        nome,
        idade,
        altura);
    return 0;
}