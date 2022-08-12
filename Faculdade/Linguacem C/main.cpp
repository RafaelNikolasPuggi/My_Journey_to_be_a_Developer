#include <iostream>
#include <stdio.h>
#include <string.h>

int main(){

	int valor1, valor2, soma;
	
	printf("Leia valor 1 \n");
	scanf("%i", &valor1);
	printf("Leia valor 2 \n");
	scanf("%i", &valor2);
	
	soma = valor1 + valor2;
	printf("Valores somados: %i \n", soma);

return 0;
}
