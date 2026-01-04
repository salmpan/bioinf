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

	for (int i = 0; i < length-4; i++) {
		if(seq[i  ] == 'F' &&
		   seq[i+1] == 'L' &&
		   seq[i+2] == 'A' &&
		   seq[i+3] == 'R' &&
                   seq[i+4] == 'E') {
			printf("Found it at %d\n", i+1);
		}
	}
}
