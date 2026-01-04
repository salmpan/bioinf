#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main() {
	char seq[1000];
	printf("Enter sequence: ");
	scanf("%s", seq);

	int length = strlen(seq);
	if(length < 3) {
		printf("\nEisai stokos");
		exit(1);
	}

	printf("The length was: %d\n", length);


	if (seq[0] == 'A' && seq[1] == 'T' && seq[2] == 'C') {
		printf("Starts with ATC");
		exit(0);
	}

	printf("Doesn't start with ATC");
}
