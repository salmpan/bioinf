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


	if (seq[length-3] == 'E' && seq[length-2] == 'A' && seq[length-1] == 'A') {
		printf("Ends with EAA");
		exit(0);
	}

	printf("Doesn't end with EAA");
}
