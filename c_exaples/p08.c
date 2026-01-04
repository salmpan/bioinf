
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main() {
	char seq[1000];

	scanf("%s", seq);

	int length = strlen(seq);

	printf("The length was: %d\n", length);


	if(length < 5) {
		printf("You are an idiot.\n");
		exit(1);
	}

	for (int i = 0; i < length; i++) {
		if(seq[i] == 'F') {
			printf("Found it at %d\n", i+1);
		}
	}
}
