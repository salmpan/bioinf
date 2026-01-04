#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main() {
	char seq[1000];
	printf("Enter the target sequence: ");
	scanf("%s", seq);
	int length1 = strlen(seq);
	
	char penta[100];
	printf("\nEnter the pentapeptide: ");
	scanf("%s", penta);
	int length2 = strlen(penta);

        printf("\nThe length of the target sequence was: %d", length1);

	if(length1 < 5) {
		printf("\nYou are an idiot.");
		exit(1);
	}

	if(length2 != 5) {
		printf("\nEisai boubounas.");
		exit(1);
	}


	for (int i = 0; i < length1-4; i++) {
		if(seq[i  ] == penta[0] &&
		   seq[i+1] == penta[1] &&
		   seq[i+2] == penta[2] &&
		   seq[i+3] == penta[3] &&
                   seq[i+4] == penta[4]) {
			printf("\nFound it at %d", i+1);
		}
	}
}
