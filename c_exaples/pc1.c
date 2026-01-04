#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main() {
	char seq[1000];
	scanf("%s", seq);

	int length = strlen(seq);

	printf("The length was: %d\n", length);

	int charge = 0;
	for (int i = 0; i < length; i++) {
		if (seq[i] == 'K' || seq[i] == 'R') {
			charge++;
		}

		if (seq[i] == 'D' || seq[i] == 'E') {
			charge--;
		}
	}

	printf("The total charge is: %d\n", charge);
}
