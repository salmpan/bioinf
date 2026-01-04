#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main() {
	char seq[1000];
	printf("Enter the target sequence: ");
	scanf("%s", seq);
	int length1 = strlen(seq);
	
	char peptide[100];
	printf("\nEnter the peptide: ");
	scanf("%s", peptide);
	int length2 = strlen(peptide);

        printf("\nThe length of the target sequence was: %d", length1);

	/*
	if(length1 < 5) {
		printf("\nYou are an idiot.");
		exit(1);
	}
	*/
	
	if(length2 > length1) {
		printf("\nEisai boubounas.");
		exit(1);
	}


	for (int i = 0; i < length1-length2+1; i++) {
		int found = 0;
		for(int j = 0; j < length2; j++) {
			if(seq[i+j] == peptide[j]) {
				found++;
			} 
		}

		if(found == length2) {
			printf("\nFound it at: %d", i+1);
		}
	}
}
 
